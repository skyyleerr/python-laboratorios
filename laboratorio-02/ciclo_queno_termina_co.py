numero = 1

while numero <= 5:
    print(numero)
    numero += 1

# 1
# 2
# 3
# 4
# 5

# ¿Por qué funciona ahora?
# La instrucción:
# numero += 1# ...incrementa la variable que controla el ciclo en cada vuelta. Así numero llega a 6,
# la condición numero <= 5 deja de cumplirse y el ciclo termina.
