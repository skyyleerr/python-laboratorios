import calculos
import validaciones


def leer_float(mensaje, regla, texto_error):
    while True:
        try:
            valor = float(input(mensaje))
        except ValueError:
            print("Debes escribir un número válido.")
            continue
        if not regla(valor):
            print(texto_error)
            continue
        return valor


def leer_entero(mensaje, regla, texto_error):
    while True:
        try:
            valor = int(input(mensaje))
        except ValueError:
            print("Debes escribir un número entero.")
            continue
        if not regla(valor):
            print(texto_error)
            continue
        return valor


def formato_numero(valor):
    return int(valor) if isinstance(valor, float) and valor.is_integer() else valor


def main():
    precio = leer_float("Precio: ", validaciones.precio_valido, "El precio debe ser mayor que cero.")
    cantidad = leer_entero("Cantidad: ", validaciones.cantidad_valida, "La cantidad no puede ser negativa.")
    descuento_porcentaje = leer_float("Descuento (%): ", validaciones.porcentaje_valido, "El porcentaje debe estar entre 0 y 100.")
    impuesto_porcentaje = leer_float("Impuesto (%): ", validaciones.porcentaje_valido, "El porcentaje debe estar entre 0 y 100.")

    subtotal = calculos.calcular_subtotal(precio, cantidad)
    descuento = calculos.calcular_descuento(subtotal, descuento_porcentaje)
    base = subtotal - descuento
    impuesto = calculos.calcular_impuesto(base, impuesto_porcentaje)
    total = base + impuesto

    print("Subtotal:", formato_numero(subtotal))
    print("Descuento:", formato_numero(descuento))
    print("Base después del descuento:", formato_numero(base))
    print("Impuesto:", formato_numero(impuesto))
    print("Total:", formato_numero(total))


if __name__ == "__main__":
    main()
