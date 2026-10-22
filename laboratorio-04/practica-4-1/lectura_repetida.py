import math
while True:
    try:
        precio = float(input("Precio: "))
    except ValueError:
        print("Debes escribir un número.")
        continue
    if not math.isfinite(precio) or precio <= 0:
        print("El precio debe ser finito y positivo.")
        continue
    print("Precio aceptado:", precio)
    break
