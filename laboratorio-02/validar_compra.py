# Práctica 2.2 - Validar antes de calcular
precio = float(input("Precio: "))
cantidad = int(input("Cantidad: "))
descuento = float(input("Descuento (%): "))

if precio <= 0 or cantidad <= 0:
    print("El precio y la cantidad deben ser mayores que cero.")
elif descuento < 0 or descuento > 100:
    print("El descuento debe estar entre 0 y 100.")
else:
    subtotal = precio * cantidad
    valor_descuento = subtotal * descuento / 100
    total = subtotal - valor_descuento

    print("Subtotal:", subtotal)
    print("Descuento:", valor_descuento)
    print("Total:", total)

# Casos: (100000, 2, 10) -> total 180000.0 | (-50000, 2, 10) -> rechaza precio
#        (50000, 0, 5) -> rechaza cantidad | (80000, 1, 110) -> rechaza descuento
