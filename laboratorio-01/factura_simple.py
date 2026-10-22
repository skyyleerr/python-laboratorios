nombre_producto = "Producto"
precio_unitario = 100000.0
cantidad = 2
descuento = 0.10

subtotal = precio_unitario * cantidad
valor_descuento = subtotal * descuento
total = subtotal - valor_descuento

print("Subtotal: $" + str(subtotal))
print("Descuento: $" + str(valor_descuento))
print("Total: $" + str(total))

''''''

nombre_producto = "Producto"
precio_unitario = 100000.0
cantidad = 2
descuento = 0.10
impuesto = 0.19

subtotal = precio_unitario * cantidad
valor_descuento = subtotal * descuento
base_descuento = subtotal - valor_descuento
valor_impuesto = base_descuento * impuesto
total_final = base_descuento + valor_impuesto

print("Subtotal: $" + str(subtotal))
print("Descuento: $" + str(valor_descuento))
print("Base después del descuento: $" + str(base_descuento))
print("Impuesto: $" + str(valor_impuesto))
print("Total final: $" + str(total_final))