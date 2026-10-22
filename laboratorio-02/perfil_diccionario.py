aprendiz = {
    "ficha": 3388087,
    "nombre": "Anthony",
    "trimestre": 6,
    "promedio": 4.5,
    "activo": True
}

# Mostrar el nombre del aprendiz
print("Nombre:", aprendiz["nombre"])

# Cambiar el trimestre
aprendiz["trimestre"] = 7

# Agregar el correo electrónico
aprendiz["correo"] = "anthony@gmail.com"

# Mostrar el perfil actualizado
print("\nPerfil actualizado:")
print(aprendiz)

# C:\Users\Asus\Downloads\python-laboratorio-02>C:\Users\Asus\AppData\Local\Programs\Python\Python315\python.exe c:/Users/Asus/Downloads/python-laboratorio-02/perfil_diccionario.py
# Nombre: Anthony

# Perfil actualizado:
# {'ficha': 3388087, 'nombre': 'Anthony', 'trimestre': 7, 'promedio': 4.5, 'activo': True, 'correo': 'anthony@gmail.com'}