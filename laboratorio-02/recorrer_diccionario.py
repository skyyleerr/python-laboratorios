producto = {
    "codigo": "P001",
    "nombre": "Teclado",
    "precio": 85000.0
}

# Recorrer las claves
print("Claves del producto:")
for clave in producto:
    print(clave)

# Recorrer los valores
print("\nValores del producto:")
for valor in producto.values():
    print(valor)

# Recorrer las claves y los valores
print("\nClaves y valores:")
for clave, valor in producto.items():
    print(clave, ":", valor)


# C:\Users\Asus\Downloads\python-laboratorio-02>C:\Users\Asus\AppData\Local\Programs\Python\Python315\python.exe c:/Users/Asus/Downloads/python-laboratorio-02/recorrer_diccionario.py
# Claves del producto:
# codigo
# nombre
# precio

# Valores del producto:
# P001
# Teclado
# 85000.0

# Claves y valores:
# codigo : P001
# nombre : Teclado
# precio : 85000.0