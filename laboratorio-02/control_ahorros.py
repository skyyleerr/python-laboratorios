
total = 0
contador = 0

deposito = float(input("Depósito (0 para terminar): "))

while deposito != 0:
    if deposito < 0:
        print("El depósito debe ser positivo.")
    else:
        total += deposito
        contador += 1
        print("Ahorro acumulado:", total)

    print()
    deposito = float(input("Depósito (0 para terminar): "))

print()
print("Depósitos válidos:", contador)
print("Total ahorrado:", total)

# C:\Users\Asus\Downloads\python-laboratorio-02>C:\Users\Asus\AppData\Local\Programs\Python\Python315\python.exe c:/Users/Asus/Downloads/python-laboratorio-02/control_ahorros.py
# Depósito (0 para terminar): 10000
# Ahorro acumulado: 10000.0

# Depósito (0 para terminar): -5000
# El depósito debe ser positivo.

# Depósito (0 para terminar): 25000
# Ahorro acumulado: 35000.0

# Depósito (0 para terminar): 0

# Depósitos válidos: 2
# Total ahorrado: 35000.0