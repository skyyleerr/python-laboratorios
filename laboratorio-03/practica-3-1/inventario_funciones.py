def mostrar_productos(productos):
    for producto in productos:
        print(producto)


def buscar_producto(productos, codigo):
    for producto in productos:
        if producto["codigo"] == codigo:
            return producto
    return None


def valor_inventario(productos):
    return sum(producto["precio"] * producto["cantidad"] for producto in productos)


def productos_sin_stock(productos):
    return [producto["nombre"] for producto in productos if producto["cantidad"] == 0]


if __name__ == "__main__":
    inventario = [
        {"codigo": "P001", "nombre": "Teclado", "precio": 85000, "cantidad": 4},
        {"codigo": "P002", "nombre": "Mouse", "precio": 45000, "cantidad": 0},
        {"codigo": "P003", "nombre": "Monitor", "precio": 700000, "cantidad": 2},
    ]

    print("Productos:")
    mostrar_productos(inventario)
    print("Búsqueda P002:", buscar_producto(inventario, "P002"))
    print("Búsqueda P999:", buscar_producto(inventario, "P999"))
    print("Valor del inventario:", valor_inventario(inventario))
    print("Sin stock:", productos_sin_stock(inventario))
