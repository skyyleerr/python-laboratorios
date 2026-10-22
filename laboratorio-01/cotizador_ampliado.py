# Cotizador de compra - Reto de ampliación (Práctica 1.5)
# Agrega: código de cotización, vendedor y costo de envío.
# El envío se suma DESPUÉS de calcular el impuesto.

codigo = input("Código de la cotización: ")
vendedor = input("Nombre del vendedor: ")
nombre_cliente = input("Nombre del cliente: ")
producto = input("Producto: ")
precio_unitario = float(input("Precio unitario: "))
cantidad = int(input("Cantidad: "))
descuento = float(input("Descuento (%): "))
impuesto = float(input("Impuesto (%): "))
costo_envio = float(input("Costo de envío: "))

subtotal = precio_unitario * cantidad
valor_descuento = subtotal * (descuento / 100)
base = subtotal - valor_descuento
valor_impuesto = base * (impuesto / 100)
total_sin_envio = base + valor_impuesto
total = total_sin_envio + costo_envio

print()
print("=============================")
print("      COTIZADOR PYTHON")
print("=============================")
print(f"Cotización: {codigo}")
print(f"Vendedor: {vendedor}")
print("-----------------------------")
print("      RESUMEN DE COMPRA")
print("-----------------------------")
print(f"Cliente: {nombre_cliente}")
print(f"Producto: {producto}")
print(f"Precio unitario: ${precio_unitario}")
print(f"Cantidad: {cantidad}")
print(f"Subtotal: ${subtotal}")
print(f"Descuento: ${valor_descuento}")
print(f"Base: ${base}")
print(f"Impuesto: ${valor_impuesto}")
print(f"Envío: ${costo_envio}")
print(f"TOTAL: ${total}")
