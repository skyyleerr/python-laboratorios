notas = [2.5, 3.8, 4.1]

estados = [
    "Aprobado" if nota >= 3.0 else "No aprobado"
    for nota in notas
]

print(estados)

# C:\Users\Asus\Downloads\python-laboratorio-02>C:\Users\Asus\AppData\Local\Programs\Python\Python315\python.exe c:/Users/Asus/Downloads/python-laboratorio-02/estados_notas.py
# ['No aprobado', 'Aprobado', 'Aprobado']