grupos = [[1, 2], [3, 4], [5, 6]]

numeros = [
    numero
    for grupo in grupos
    for numero in grupo
]

print(numeros)

# C:\Users\Asus\Downloads\python-laboratorio-02>C:\Users\Asus\AppData\Local\Programs\Python\Python315\python.exe c:/Users/Asus/Downloads/python-laboratorio-02/numeros_anidados.py
# [1, 2, 3, 4, 5, 6]