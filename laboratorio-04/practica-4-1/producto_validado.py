import math

class Producto:
    def __init__(self, nombre, precio):
        if not isinstance(nombre, str) or not nombre.strip():
            raise ValueError("El nombre es obligatorio.")
        if isinstance(precio, bool) or not isinstance(precio, (int, float)):
            raise TypeError("El precio debe ser numérico.")
        if not math.isfinite(precio) or precio <= 0:
            raise ValueError("El precio debe ser finito y positivo.")
        self.nombre = nombre.strip()
        self.precio = float(precio)

try:
    producto = Producto("Teclado", -5000)
    print(producto.nombre)
except (ValueError, TypeError) as error:
    print("No se pudo crear:", error)
