import math
from pathlib import Path
ruta = Path(__file__).resolve().parent / "operaciones.txt"
while True:
    print("\n1. Registrar operación\n2. Mostrar historial\n3. Salir")
    opcion = input("Opción: ").strip()
    if opcion == "1":
        concepto = input("Concepto: ").strip().replace("|", "/")
        try:
            valor = float(input("Valor: "))
        except ValueError:
            print("Valor inválido.")
            continue
        if not math.isfinite(valor):
            print("El valor debe ser finito.")
            continue
        if not concepto:
            print("El concepto es obligatorio.")
            continue
        with ruta.open("a", encoding="utf-8") as archivo:
            archivo.write(f"{concepto} | {valor:.2f}\n")
        print("Operación guardada.")
    elif opcion == "2":
        try:
            print(ruta.read_text(encoding="utf-8"))
        except FileNotFoundError:
            print("Todavía no hay operaciones registradas.")
    elif opcion == "3":
        print("Fin del historial.")
        break
    else:
        print("Opción no válida.")
