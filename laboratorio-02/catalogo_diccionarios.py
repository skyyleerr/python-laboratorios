productos = [
    {"codigo": "P001", "nombre": "Teclado", "precio": 85000.0, "cantidad": 4},
    {"codigo": "P002", "nombre": "Mouse", "precio": 45000.0, "cantidad": 7},
    {"codigo": "P003", "nombre": "Monitor", "precio": 700000.0, "cantidad": 2}
]

# Solicitar los datos del cuarto producto
print("Registro de un nuevo producto")

codigo = input("Ingrese el código: ")
nombre = input("Ingrese el nombre: ")
precio = float(input("Ingrese el precio: "))
cantidad = int(input("Ingrese la cantidad: "))

# Construir el nuevo diccionario
nuevo_producto = {
    "codigo": codigo,
    "nombre": nombre,
    "precio": precio,
    "cantidad": cantidad
}

# Agregar el producto a la lista
productos.append(nuevo_producto)

# Mostrar todos los productos
print("\nCatálogo de productos:")

for producto in productos:
    print("--------------------")
    for clave, valor in producto.items():
        print(clave, ":", valor)

# C:\Users\Asus\Downloads\python-laboratorio-02>C:\Users\Asus\AppData\Local\Programs\Python\Python315\python.exe c:/Users/Asus/Downloads/python-laboratorio-02/catalogo_diccionarios.py
# Registro de un nuevo producto
# Ingrese el código: P004
# Ingrese el nombre: Audífonos
# Ingrese el precio: 60000
# Ingrese la cantidad: 3

# Catálogo de productos:
# --------------------
# codigo : P001
# nombre : Teclado
# precio : 85000.0
# cantidad : 4
# --------------------
# codigo : P002
# nombre : Mouse
# precio : 45000.0
# cantidad : 7
# --------------------
# codigo : P003
# nombre : Monitor
# precio : 700000.0
# cantidad : 2
# --------------------
# codigo : P004
# nombre : Audífonos
# precio : 60000.0
# cantidad : 3