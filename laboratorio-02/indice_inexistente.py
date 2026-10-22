# Práctica 2.4 - Depuración: índice inexistente
productos = ["Teclado", "Mouse", "Monitor"]

# La lista tiene 3 elementos; los índices válidos son 0, 1 y 2 (o -1 para el último).
# Original: print(productos[3])  ->  IndexError: list index out of range
print(productos[len(productos) - 1])   # último elemento: Monitor
print(productos[-1])                   # equivalente
