total = 0

numero = int(input("Número (0 para terminar): "))

while numero != 0:
    total += numero
    print("Acumulado:", total)
    numero = int(input("Número (0 para terminar): "))

print("Total final:", total)

# Número (0 para terminar): 10
# Acumulado: 10
# Número (0 para terminar): 25
# Acumulado: 35
# Número (0 para terminar): -5
# Acumulado: 30
# Número (0 para terminar): 0
# Total final: 30