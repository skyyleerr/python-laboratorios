from pathlib import Path
ruta = Path(__file__).resolve().parent / "historial.txt"
# Modo a agrega y conserva las entradas existentes.
with ruta.open("a", encoding="utf-8") as archivo:
    archivo.write("Registro agregado\n")
print(ruta.read_text(encoding="utf-8"))
