from pathlib import Path
ruta = Path(__file__).resolve().parent / "mensaje.txt"
try:
    print("Contenido:")
    print(ruta.read_text(encoding="utf-8"))
except FileNotFoundError:
    print("Todavía no se ha creado mensaje.txt. Ejecuta escribir_archivo.py.")
