ventas = [
    {"producto": "Teclado", "categoria": "Periféricos", "total": 150000},
    {"producto": "Mouse", "categoria": "Periféricos", "total": 70000},
    {"producto": "Disco SSD", "categoria": "Componentes", "total": 280000},
    {"producto": "Memoria USB", "categoria": "Accesorios", "total": 45000}
]

# 1. Productos con ventas superiores a $100.000
productos_destacados = [
    venta["producto"]
    for venta in ventas
    if venta["total"] > 100000
]

print("Productos con ventas superiores a $100.000:", productos_destacados)

# 2. Categorías diferentes
categorias = {
    venta["categoria"]
    for venta in ventas
}

print("Categorías diferentes:", categorias)

# 3. Diccionario de producto y valor de venta
valores_venta = {
    venta["producto"]: venta["total"]
    for venta in ventas
}

print("Valores de venta:", valores_venta)

# 4. Suma de todas las ventas
valores = [
    venta["total"]
    for venta in ventas
]

total_ventas = sum(valores)

print("Total de ventas:", total_ventas)

# C:\Users\Asus\Downloads\python-laboratorio-02>C:\Users\Asus\AppData\Local\Programs\Python\Python315\python.exe c:/Users/Asus/Downloads/python-laboratorio-02/informe_comprensiones.py
# Productos con ventas superiores a $100.000: ['Teclado', 'Disco SSD']
# Categorías diferentes: {'Periféricos', 'Accesorios', 'Componentes'}
# Valores de venta: {'Teclado': 150000, 'Mouse': 70000, 'Disco SSD': 280000, 'Memoria USB': 45000}
# Total de ventas: 545000