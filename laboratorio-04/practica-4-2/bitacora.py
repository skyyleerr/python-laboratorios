from pathlib import Path
ruta = Path(__file__).resolve().parent / "pruebas.txt"
nombre = input("Nombre de la prueba: ").strip()
resultado = input("Resultado (aprobada/fallida): ").strip().lower()
observacion = input("Observación: ").strip().replace("|", "/")
if not nombre or resultado not in {"aprobada", "fallida"}:
    print("Nombre obligatorio y resultado aprobada/fallida.")
else:
    with ruta.open("a", encoding="utf-8") as archivo:
        archivo.write(f"{nombre} | {resultado} | {observacion}\n")
    print("Registro agregado a", ruta)
