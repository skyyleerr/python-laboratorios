from pathlib import Path
ruta = Path(__file__).resolve().parent / "notas.txt"
with ruta.open("w", encoding="utf-8") as archivo:
    archivo.write("Primera observación\n")
    archivo.write("Segunda observación\n")
with ruta.open("r", encoding="utf-8") as archivo:
    contenido = archivo.read()
print(contenido)
