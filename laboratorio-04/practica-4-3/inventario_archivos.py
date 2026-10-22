"""Reto sin clases: JSON como fuente persistente y CSV como exportación."""
import csv, json
from pathlib import Path
base = Path(__file__).resolve().parent
ruta_json, ruta_csv = base / "inventario.json", base / "inventario.csv"
try:
    with ruta_json.open(encoding="utf-8") as archivo:
        productos = json.load(archivo)
    if not isinstance(productos, list) or any(not isinstance(p, dict) for p in productos):
        raise ValueError("La estructura JSON debe ser una lista de objetos.")
except FileNotFoundError:
    productos = []
    print("Inventario nuevo.")
except (json.JSONDecodeError, ValueError) as error:
    print("No se altera el JSON dañado:", error)
    raise SystemExit(1)

if not productos:
    productos = [
        {"codigo": "P001", "nombre": "Teclado", "categoria": "Periféricos", "precio": 85000.0, "cantidad": 4},
        {"codigo": "P002", "nombre": "Mouse", "categoria": "Periféricos", "precio": 45000.0, "cantidad": 0},
    ]
    with ruta_json.open("w", encoding="utf-8") as archivo:
        json.dump(productos, archivo, ensure_ascii=False, indent=2)

campos = ["codigo", "nombre", "categoria", "precio", "cantidad"]
with ruta_csv.open("w", newline="", encoding="utf-8") as archivo:
    escritor = csv.DictWriter(archivo, fieldnames=campos)
    escritor.writeheader(); escritor.writerows(productos)
print("Recuperados:", len(productos), "Exportado:", ruta_csv)
