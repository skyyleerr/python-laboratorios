producto = {
    "codigo": "P001",
    "nombre": "Teclado",
    "precio": 85000.0,
    "cantidad": 4,
    "categoria": "Periféricos"
}

print(producto)
print(producto["nombre"])
print(producto["precio"])

# C:\Users\Asus\Downloads\python-laboratorio-02>C:\Users\Asus\AppData\Local\Programs\Python\Python315\python.exe c:/Users/Asus/Downloads/python-laboratorio-02/primer_diccionario.py
# {'codigo': 'P001', 'nombre': 'Teclado', 'precio': 85000.0, 'cantidad': 4, 'categoria': 'Periféricos'}
# Teclado
# 85000.0


producto = {
    "codigo": "P001",
    "nombre": "Teclado",
    "precio": 85000.0,
    "cantidad": 4,
    "categoria": "Periféricos"
}

# Modificar una clave existente
producto["cantidad"] = 8

# Agregar una nueva clave
producto["activo"] = True

# Mostrar el diccionario actualizado
print(producto)

# Consultar una clave que podría no existir
print(producto.get("marca"))

# Consultar una clave con un valor predeterminado
print(producto.get("marca", "Sin marca"))
