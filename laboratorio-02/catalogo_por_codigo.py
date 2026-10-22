productos = [
    {"codigo": "P001", "nombre": "Teclado"},
    {"codigo": "P002", "nombre": "Mouse"},
    {"codigo": "P003", "nombre": "Monitor"}
]

catalogo = {
    producto["codigo"]: producto["nombre"]
    for producto in productos
}

print(catalogo)

# C:\Users\Asus\Downloads\python-laboratorio-02>C:\Users\Asus\AppData\Local\Programs\Python\Python315\python.exe c:/Users/Asus/Downloads/python-laboratorio-02/catalogo_por_codigo.py
# {'P001': 'Teclado', 'P002': 'Mouse', 'P003': 'Monitor'}