from operaciones import calcular_subtotal, calcular_descuento


if __name__ == "__main__":
    subtotal = calcular_subtotal(40000, 2)
    descuento = calcular_descuento(subtotal, 5)
    print(subtotal - descuento)
