nombre_cliente = input("Nombre del cliente: ")
producto = input("Producto: ")
precio_unitario = float(input("Precio unitario: "))
cantidad = int(input("Cantidad: "))
descuento = float(input("Descuento (%): "))
impuesto = float(input("Impuesto (%): "))

subtotal = precio_unitario * cantidad

descuento_decimal = descuento / 100
valor_descuento = subtotal * descuento_decimal

base = subtotal - valor_descuento

impuesto_decimal = impuesto / 100
valor_impuesto = base * impuesto_decimal

total = base + valor_impuesto

print("=============================")
print("      COTIZADOR PYTHON")
print("=============================")
print()
print("-----------------------------")
print("      RESUMEN DE COMPRA")
print("-----------------------------")
print("Cliente:", nombre_cliente)
print("Producto:", producto)
print("Precio unitario: $", precio_unitario)
print("Cantidad:", cantidad)
print("Subtotal: $", subtotal)
print("Descuento: $", valor_descuento)
print("Base: $", base)
print("Impuesto: $", valor_impuesto)
print("TOTAL: $", total)