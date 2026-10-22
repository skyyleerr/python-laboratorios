producto = {
    "codigo": "P001",
    "nombre": "Teclado",
    "precio": 85000.0,
    "cantidad": 4
}

# Solicitar el nuevo precio
nuevo_precio = float(input("Ingrese el nuevo precio: "))

# Validar y actualizar únicamente el precio
if nuevo_precio > 0:
    producto["precio"] = nuevo_precio
    print("Precio actualizado correctamente.")
else:
    print("Error: el precio debe ser mayor que cero.")

# Mostrar todos los pares clave-valor
print("\nDatos del producto:")
for clave, valor in producto.items():
    print(clave, ":", valor)


# C:\Users\Asus\Downloads\python-laboratorio-02>C:\Users\Asus\AppData\Local\Programs\Python\Python315\python.exe c:/Users/Asus/Downloads/python-laboratorio-02/actualizar_producto.py
# Ingrese el nuevo precio: 75000
# Precio actualizado correctamente.

# Datos del producto:
# codigo : P001
# nombre : Teclado
# precio : 75000.0
# cantidad : 4