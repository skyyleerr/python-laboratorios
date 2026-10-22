import math

compras = []
while True:
    try:
        importe = float(input("Importe (0 para terminar): "))
    except ValueError:
        print("Importe inválido; intenta de nuevo.")
        continue
    if not math.isfinite(importe):
        print("El importe debe ser un número finito.")
        continue
    if importe == 0:
        break
    if importe < 0:
        print("No se aceptan valores negativos.")
        continue
    compras.append(importe)
print("Compras aceptadas:", len(compras))
print("Suma acumulada:", sum(compras))
