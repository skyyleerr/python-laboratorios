class Inventario:
    def __init__(self):
        self.productos = []  # Corrección: la lista se crea para cada inventario.

    def agregar(self, producto):
        self.productos.append(producto)


if __name__ == "__main__":
    primero = Inventario()
    segundo = Inventario()
    primero.agregar("Teclado")
    print("Primero:", primero.productos)
    print("Segundo:", segundo.productos)
