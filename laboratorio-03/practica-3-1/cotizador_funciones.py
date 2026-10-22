def calcular_subtotal(precio, cantidad):
    return precio * cantidad


def calcular_descuento(subtotal, porcentaje):
    return subtotal * porcentaje / 100


def calcular_impuesto(base, porcentaje):
    return base * porcentaje / 100


def formato_numero(valor):
    """Muestra importes enteros sin el sufijo .0 cuando corresponde."""
    return int(valor) if isinstance(valor, float) and valor.is_integer() else valor


if __name__ == "__main__":
    precio = 100000
    cantidad = 2
    porcentaje_descuento = 10
    porcentaje_impuesto = 19

    subtotal = calcular_subtotal(precio, cantidad)
    descuento = calcular_descuento(subtotal, porcentaje_descuento)
    base_despues_descuento = subtotal - descuento
    impuesto = calcular_impuesto(base_despues_descuento, porcentaje_impuesto)
    total = base_despues_descuento + impuesto

    print("Subtotal:", formato_numero(subtotal))
    print("Descuento:", formato_numero(descuento))
    print("Base después del descuento:", formato_numero(base_despues_descuento))
    print("Impuesto:", formato_numero(impuesto))
    print("Total:", formato_numero(total))
