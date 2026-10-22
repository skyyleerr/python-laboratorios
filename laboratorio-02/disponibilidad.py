unidades_disponibles = 12
unidades_solicitadas = 8

hay_suficientes = unidades_disponibles >= unidades_solicitadas
cantidades_iguales = unidades_disponibles == unidades_solicitadas
se_solicitaron_mas = unidades_solicitadas > unidades_disponibles

print("¿Hay suficientes unidades?", hay_suficientes)
print("¿Las cantidades son iguales?", cantidades_iguales)
print("¿Se solicitaron más unidades?", se_solicitaron_mas)

# ¿Hay suficientes unidades? True
# ¿Las cantidades son iguales? False
# ¿Se solicitaron más unidades? False

''''''

unidades_solicitadas = 12

# ¿Hay suficientes unidades? True
# ¿Las cantidades son iguales? True
# ¿Se solicitaron más unidades? False

''''''

unidades_solicitadas = 15

# ¿Hay suficientes unidades? False
# ¿Las cantidades son iguales? False
# ¿Se solicitaron más unidades? True