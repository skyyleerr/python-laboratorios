nombres = ["  ana ", "CARLOS", " Laura ", ""]

normalizados = [
    nombre.strip().title()
    for nombre in nombres
    if nombre.strip() != ""
]

print(normalizados)

# C:\Users\Asus\Downloads\python-laboratorio-02>C:\Users\Asus\AppData\Local\Programs\Python\Python315\python.exe c:/Users/Asus/Downloads/python-laboratorio-02/nombres_normalizados.py
# ['Ana', 'Carlos', 'Laura']