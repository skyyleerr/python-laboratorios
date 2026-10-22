import csv
from pathlib import Path
ruta = Path(__file__).resolve().parent / "reporte.csv"
try:
    with ruta.open(newline="", encoding="utf-8") as archivo:
        for producto in csv.DictReader(archivo):
            print(producto["codigo"], producto["nombre"], producto["precio"])
except FileNotFoundError:
    print("Primero ejecuta exportar_csv.py.")
