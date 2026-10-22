from pathlib import Path
base = Path(__file__).resolve().parent
carpeta = base / "reportes"
carpeta.mkdir(parents=True, exist_ok=True)
ruta = carpeta / "resumen.txt"
lineas = ["Reporte de inventario", "Productos: 0", "Valor total: $0"]
ruta.write_text("\n".join(lineas) + "\n", encoding="utf-8")
print(ruta.read_text(encoding="utf-8"))
print("Guardado en:", ruta.resolve())
