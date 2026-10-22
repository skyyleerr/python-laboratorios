import json
from pathlib import Path
productos = [
    {"codigo": "P001", "nombre": "Teclado", "precio": 85000, "cantidad": 4},
    {"codigo": "P002", "nombre": "Mouse", "precio": 45000, "cantidad": 0},
]
ruta = Path(__file__).resolve().parent / "productos.json"
with ruta.open("w", encoding="utf-8") as archivo:
    json.dump(productos, archivo, ensure_ascii=False, indent=4)
print("Productos guardados en", ruta)
