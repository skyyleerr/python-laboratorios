"""Exportación CSV de solo lectura desde la interfaz pública de Inventario."""
import csv
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent
RUTA_CSV = BASE_DIR / "reportes" / "inventario.csv"
CAMPOS = ["codigo", "nombre", "categoria", "precio", "cantidad", "valor_inventario"]

def exportar_csv(inventario, ruta=RUTA_CSV):
    ruta = Path(ruta)
    ruta.parent.mkdir(parents=True, exist_ok=True)
    filas = []
    for producto in inventario.listar_productos():
        filas.append({
            "codigo": producto.codigo,
            "nombre": producto.nombre,
            "categoria": producto.categoria,
            "precio": producto.precio,
            "cantidad": producto.cantidad,
            "valor_inventario": producto.calcular_valor(),
        })
    with ruta.open("w", newline="", encoding="utf-8") as archivo:
        escritor = csv.DictWriter(archivo, fieldnames=CAMPOS)
        escritor.writeheader()
        escritor.writerows(filas)
    return ruta
