import csv
from pathlib import Path
base = Path(__file__).resolve().parent
ventas = [
    {"codigo": "V001", "producto": "Teclado", "cantidad": 2, "total": 170000},
    {"codigo": "V002", "producto": "Mouse", "cantidad": 3, "total": 135000},
    {"codigo": "V003", "producto": "Monitor", "cantidad": 1, "total": 420000},
    {"codigo": "V004", "producto": "Cable", "cantidad": 5, "total": 50000},
]
ruta = base / "ventas.csv"
campos = ["codigo", "producto", "cantidad", "total"]
with ruta.open("w", newline="", encoding="utf-8") as archivo:
    escritor = csv.DictWriter(archivo, fieldnames=campos)
    escritor.writeheader()
    escritor.writerows(ventas)
with ruta.open(newline="", encoding="utf-8") as archivo:
    recuperadas = list(csv.DictReader(archivo))
total_vendido = sum(float(fila["total"]) for fila in recuperadas)
print("Ventas leídas:", len(recuperadas))
print("Total vendido:", total_vendido)
