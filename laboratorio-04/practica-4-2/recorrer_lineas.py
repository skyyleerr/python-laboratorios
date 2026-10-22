from pathlib import Path
ruta = Path(__file__).resolve().parent / "pruebas.txt"
try:
    with ruta.open("r", encoding="utf-8") as archivo:
        for numero, linea in enumerate(archivo, start=1):
            print(numero, "-", linea.strip())
except FileNotFoundError:
    print("La bitácora todavía no existe.")
