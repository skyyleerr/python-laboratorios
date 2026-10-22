# Práctica 2.4 - Cortes, orden y copias
productos = ["Teclado", "Mouse", "Monitor", "Cámara", "Parlantes"]

print(productos[0:2])
print(productos[2:])
print(productos[:3])
print(productos[-2:])

otros = ["Monitor", "Cámara", "Teclado"]
ordenados = sorted(otros)
print("Original:", otros)
print("Ordenados:", ordenados)

# Compartir la misma lista
original = ["Teclado", "Mouse"]
otra_referencia = original
otra_referencia.append("Monitor")
print(original)           # ['Teclado', 'Mouse', 'Monitor'] -> se modificó

# Copiar de verdad
original = ["Teclado", "Mouse"]
copia = original.copy()
copia.append("Monitor")
print("Original:", original)  # sin cambios
print("Copia:", copia)
