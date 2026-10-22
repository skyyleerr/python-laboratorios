from pathlib import Path
ruta = Path("archivo_que_no_existe.txt")
try:
    print(ruta.read_text(encoding="utf-8"))
except FileNotFoundError:
    print("No se encontró el archivo solicitado.")
