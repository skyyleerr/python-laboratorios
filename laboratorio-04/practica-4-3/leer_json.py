import json
from pathlib import Path
ruta = Path(__file__).resolve().parent / "productos.json"
try:
    with ruta.open("r", encoding="utf-8") as archivo:
        productos = json.load(archivo)
    for producto in productos:
        print(producto["codigo"], "-", producto["nombre"])
except FileNotFoundError:
    print("Primero ejecuta primer_json.py.")
except json.JSONDecodeError as error:
    print("JSON inválido:", error)
