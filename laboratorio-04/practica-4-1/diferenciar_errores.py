try:
    int("abc")
except ValueError:
    print("El contenido no representa un entero.")

try:
    int(None)
except TypeError:
    print("El tipo recibido no permite esa conversión.")
