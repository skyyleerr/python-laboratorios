def calcular_subtotal(precio, cantidad):
    subtotal = precio * cantidad
    return subtotal


def mostrar_total(precio, cantidad):
    print(precio * cantidad)


def obtener_total(precio, cantidad):
    return precio * cantidad


if __name__ == "__main__":
    resultado = calcular_subtotal(85000, 3)
    print("Subtotal:", resultado)
    mostrar_total(10000, 3)
    total = obtener_total(10000, 3)
    print("Resultado reutilizable:", total)
