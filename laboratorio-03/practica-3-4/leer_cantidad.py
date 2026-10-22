def leer_cantidad():
    while True:
        try:
            cantidad = int(input("Cantidad: "))
        except ValueError:
            print("Debes escribir un entero.")
            continue

        if cantidad < 0:
            print("La cantidad no puede ser negativa.")
            continue

        return cantidad


if __name__ == "__main__":
    cantidad = leer_cantidad()
    print("Cantidad aceptada:", cantidad)
