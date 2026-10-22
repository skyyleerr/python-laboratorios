from inventario import Inventario
from producto import Producto


if __name__ == "__main__":
    primero = Inventario()
    segundo = Inventario()

    primero.registrar_producto(Producto("P001", "Teclado", "Periféricos", 85000, 4))

    print("Primero:", len(primero.listar_productos()))
    print("Segundo:", len(segundo.listar_productos()))
