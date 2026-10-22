def agotados_con_for(productos):
    nombres = []
    for producto in productos:
        if producto["cantidad"] == 0:
            nombres.append(producto["nombre"])
    return nombres


def agotados(productos):
    return [producto["nombre"] for producto in productos if producto["cantidad"] == 0]


if __name__ == "__main__":
    inventario = [
        {"codigo": "P001", "nombre": "Teclado", "cantidad": 4},
        {"codigo": "P002", "nombre": "Mouse", "cantidad": 0},
        {"codigo": "P003", "nombre": "Monitor", "cantidad": 0},
    ]
    print("Con for:", agotados_con_for(inventario))
    print("Con comprensión:", agotados(inventario))
