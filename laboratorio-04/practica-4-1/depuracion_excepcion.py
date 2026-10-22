# Corrección: el error de int("hola") es ValueError, no ZeroDivisionError.
try:
    numero = int("hola")
except ValueError:
    print("No se pudo convertir: el texto no representa un entero.")
