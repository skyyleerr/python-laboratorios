nombre_t = "Anthony Cordova"
horas_tb = 67
valor_h = 50000.0

pago_tt = horas_tb * valor_h

APORTE = 0.04

aporte = pago_tt * APORTE

print(f"Nombre Trabajador: {nombre_t}")
print(f"Pago Total: {pago_tt}")
print(f"Aporte: {aporte}")

''''''

unidades = 4
precio = 25000.0
descuento = 0.20

subtotal = unidades * precio
valor_descuento = subtotal * descuento
total = subtotal - valor_descuento

print(total)

#El subtotal es de: 100.000 
#El descuento es de: 20.000 
#El programa imprimirá: 80000.0