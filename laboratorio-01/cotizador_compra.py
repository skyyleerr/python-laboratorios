# Cotizador de compra - Laboratorio 01, Práctica 1.5
# Orden de cálculo:
# 1. subtotal = precio * cantidad
# 2. valor_descuento = subtotal * (descuento / 100)
# 3. base = subtotal - valor_descuento
# 4. valor_impuesto = base * (impuesto / 100)  (el impuesto se aplica sobre la base)
# 5. total = base + valor_impuesto

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
print(f"Precio unitario: ${precio_unitario}")
print("Cantidad:", cantidad)
print(f"Subtotal: ${subtotal}")
print(f"Descuento: ${valor_descuento}")
print(f"Base: ${base}")
print(f"Impuesto: ${valor_impuesto}")
print(f"TOTAL: ${total}")