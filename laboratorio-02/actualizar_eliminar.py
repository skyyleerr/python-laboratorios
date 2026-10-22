producto = {
    "codigo": "P001",
    "nombre": "Teclado",
    "precio": 85000.0,
    "cantidad": 4
}

# Actualizar el precio y la cantidad
producto.update({
    "precio": 80000.0,
    "cantidad": 5
})

# Eliminar y guardar la cantidad
cantidad_eliminada = producto.pop("cantidad")

# Mostrar los resultados
print(producto)
print("Cantidad eliminada:", cantidad_eliminada)

# C:\Users\Asus\Downloads\python-laboratorio-02>C:\Users\Asus\AppData\Local\Programs\Python\Python315\python.exe c:/Users/Asus/Downloads/python-laboratorio-02/actualizar_eliminar.py
# {'codigo': 'P001', 'nombre': 'Teclado', 'precio': 80000.0}
# Cantidad eliminada: 5