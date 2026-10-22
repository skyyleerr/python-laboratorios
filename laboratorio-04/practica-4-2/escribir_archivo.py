from pathlib import Path
ruta = Path(__file__).resolve().parent / "mensaje.txt"
ruta.write_text("Primer archivo de Python.\n", encoding="utf-8")
print("Archivo guardado:", ruta)
