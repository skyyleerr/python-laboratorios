import validaciones


def leer_float(mensaje):
    while True:
        try:
            return float(input(mensaje))
        except ValueError:
            print("Debes escribir un número válido.")


def leer_int(mensaje):
    while True:
        try:
            return int(input(mensaje))
        except ValueError:
            print("Debes escribir un entero válido.")


if __name__ == "__main__":
    nombre = input("Nombre: ")
    precio = leer_float("Precio: ")
    cantidad = leer_int("Cantidad: ")
    categoria = input("Categoría: ")

    aceptados = (
        validaciones.nombre_valido(nombre)
        and validaciones.precio_valido(precio)
        and validaciones.cantidad_valida(cantidad)
        and validaciones.categoria_valida(categoria)
    )
    print("Datos aceptados." if aceptados else "Revisa los datos.")
