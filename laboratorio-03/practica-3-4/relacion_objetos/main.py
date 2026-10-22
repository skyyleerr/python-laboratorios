from inventario import Inventario
from producto import Producto


if __name__ == "__main__":
    inventario = Inventario()
    print("Agregar P001:", inventario.agregar(Producto("P001", "Teclado")))
    print("Agregar P002:", inventario.agregar(Producto("P002", "Mouse")))
    print("Agregar duplicado P001:", inventario.agregar(Producto("P001", "Otro teclado")))

    for producto in inventario.listar():
        print(producto.codigo, "-", producto.nombre)

    encontrado = inventario.buscar_por_codigo("P002")
    print("Encontrado:", encontrado.nombre if encontrado else "no existe")
    print("Eliminar inexistente P999:", inventario.eliminar("P999"))
    print("Eliminar existente P002:", inventario.eliminar("P002"))
