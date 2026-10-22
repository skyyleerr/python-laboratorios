"""Persistencia JSON. Las rutas se resuelven respecto de este módulo."""
import json
import os
import tempfile
from pathlib import Path
from inventario import Inventario

BASE_DIR = Path(__file__).resolve().parent
RUTA_JSON = BASE_DIR / "datos" / "productos.json"

class ErrorAlmacenamiento(Exception):
    """El archivo persistente existe pero está dañado o no es válido."""

def guardar_inventario(inventario, ruta=RUTA_JSON):
    ruta = Path(ruta)
    datos = inventario.exportar_datos()
    ruta.parent.mkdir(parents=True, exist_ok=True)
    temporal = None
    try:
        # Escritura atómica: un fallo antes del replace deja intacto el original.
        with tempfile.NamedTemporaryFile("w", encoding="utf-8", dir=ruta.parent,
                                         delete=False, suffix=".tmp") as archivo:
            temporal = Path(archivo.name)
            json.dump(datos, archivo, ensure_ascii=False, indent=4, allow_nan=False)
            archivo.write("\n")
            archivo.flush()
            os.fsync(archivo.fileno())
        temporal.replace(ruta)
    except OSError:
        if temporal is not None:
            temporal.unlink(missing_ok=True)
        raise
    return ruta

def cargar_inventario(ruta=RUTA_JSON):
    ruta = Path(ruta)
    try:
        with ruta.open("r", encoding="utf-8") as archivo:
            datos = json.load(archivo)
    except FileNotFoundError:
        return Inventario()
    except (json.JSONDecodeError, UnicodeDecodeError) as error:
        raise ErrorAlmacenamiento(f"JSON dañado en {ruta}: {error}") from error
    try:
        return Inventario.desde_datos(datos)
    except (ValueError, TypeError, KeyError) as error:
        raise ErrorAlmacenamiento(f"Registros inválidos en {ruta}: {error}") from error
