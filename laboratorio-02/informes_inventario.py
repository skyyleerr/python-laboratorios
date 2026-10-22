productos = [
    {"nombre": "Teclado", "precio": 85000, "cantidad": 4},
    {"nombre": "Mouse", "precio": 45000, "cantidad": 0},
    {"nombre": "Monitor", "precio": 700000, "cantidad": 2}
]

# 1. Productos sin existencias
sin_existencias = [
    producto["nombre"]
    for producto in productos
    if producto["cantidad"] == 0
]

print("Productos sin existencias:", sin_existencias)

# 2. Productos con precio superior a $100.000
precios_altos = [
    producto["nombre"]
    for producto in productos
    if producto["precio"] > 100000
]

print("Productos con precio superior a $100.000:", precios_altos)

# 3. Valores diferentes de cantidad
cantidades = {
    producto["cantidad"]
    for producto in productos
}

print("Cantidades diferentes:", cantidades)

# 4. Diccionario de nombre y precio
catalogo = {
    producto["nombre"]: producto["precio"]
    for producto in productos
}

print("Catálogo de precios:", catalogo)

# C:\Users\Asus\Downloads\python-laboratorio-02>C:\Users\Asus\AppData\Local\Programs\Python\Python315\python.exe c:/Users/Asus/Downloads/python-laboratorio-02/informes_inventario.py
# Productos sin existencias: ['Mouse']
# Productos con precio superior a $100.000: ['Monitor']
# Cantidades diferentes: {0, 2, 4}
# Catálogo de precios: {'Teclado': 85000, 'Mouse': 45000, 'Monitor': 700000}