from pathlib import Path
ruta = Path(__file__).resolve().parent / "notas.txt"
with ruta.open("a", encoding="utf-8") as archivo:
    archivo.write("Una observación adicional\n")
print("Observación agregada a", ruta)
