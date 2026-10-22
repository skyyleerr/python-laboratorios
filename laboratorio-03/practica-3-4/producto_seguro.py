class Producto:
    def __init__(self, codigo, nombre, precio, cantidad):
        if not codigo.strip() or not nombre.strip():
            raise ValueError("El código y el nombre no pueden estar vacíos.")
        if precio <= 0:
            raise ValueError("El precio debe ser mayor que cero.")
        if not isinstance(cantidad, int) or cantidad < 0:
            raise ValueError("La cantidad debe ser un entero no negativo.")
        self._codigo = codigo.strip()
        self._nombre = nombre.strip()
        self._precio = float(precio)
        self._cantidad = cantidad

    def calcular_valor(self):
        return self._precio * self._cantidad

    @property
    def codigo(self):
        return self._codigo

    @property
    def nombre(self):
        return self._nombre

    @property
    def cantidad(self):
        return self._cantidad

    def actualizar_existencias(self, nueva_cantidad):
        if not isinstance(nueva_cantidad, int) or nueva_cantidad < 0:
            return False
        self._cantidad = nueva_cantidad
        return True

    @property
    def precio(self):
        return self._precio

    @precio.setter
    def precio(self, nuevo_precio):
        if not isinstance(nuevo_precio, (int, float)) or nuevo_precio <= 0:
            raise ValueError("El precio debe ser mayor que cero.")
        self._precio = float(nuevo_precio)


if __name__ == "__main__":
    producto = Producto("P001", "Teclado", 85000, 4)
    print(producto.calcular_valor())
    print(producto.codigo, producto.nombre, producto.cantidad)
    try:
        producto.codigo = "P999"
    except AttributeError as error:
        print("Código de solo consulta:", error)
    print("Actualizar a 10:", producto.actualizar_existencias(10), producto.cantidad)
    print("Actualizar a -5:", producto.actualizar_existencias(-5), producto.cantidad)
    producto.precio = 90000
    print("Nuevo precio:", producto.precio)
    try:
        producto.precio = -1
    except ValueError as error:
        print("Precio rechazado:", error)
