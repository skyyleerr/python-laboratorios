import json
from pathlib import Path
ruta = Path(__file__).resolve().parent / "productos.json"
try:
    with ruta.open(encoding="utf-8") as archivo:
        datos = json.load(archivo)
except FileNotFoundError:
    datos = []
    print("No existe todavía: se puede iniciar un inventario vacío.")
except json.JSONDecodeError as error:
    datos = None
    print("JSON dañado; no se sobrescribe. Revisa el archivo:", error)
else:
    if not isinstance(datos, list) or any(not isinstance(x, dict) for x in datos):
        datos = None
        print("Estructura inesperada; no se sobrescribe.")
    else:
        print("Registros válidos:", len(datos))
if datos is not None:
    print("Estado disponible para la aplicación:", datos)
