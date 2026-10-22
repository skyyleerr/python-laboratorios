productos = [
    {"nombre": "Teclado", "precio": 85000, "cantidad": 4},
    {"nombre": "Mouse", "precio": 45000, "cantidad": 0},
    {"nombre": "Monitor", "precio": 700000, "cantidad": 2}
]

# Productos que tienen existencias
disponibles = [
    producto["nombre"]
    for producto in productos
    if producto["cantidad"] > 0
]

print(disponibles)

# Valor total de cada producto en el inventario
valores = [
    producto["precio"] * producto["cantidad"]
    for producto in productos
]

print("Valor total:", sum(valores))

# C:\Users\Asus\Downloads\python-laboratorio-02>C:\Users\Asus\AppData\Local\Programs\Python\Python315\python.exe c:/Users/Asus/Downloads/python-laboratorio-02/inventario_productos.py
# ['Teclado', 'Monitor']
# Valor total: 1740000