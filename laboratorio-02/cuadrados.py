numeros = [1, 2, 3, 4, 5]
cuadrados = []

for numero in numeros:
    cuadrados.append(numero ** 2)

print(cuadrados)

# C:\Users\Asus\Downloads\python-laboratorio-02>C:\Users\Asus\AppData\Local\Programs\Python\Python315\python.exe c:/Users/Asus/Downloads/python-laboratorio-02/cuadrados.py
# [1, 4, 9, 16, 25]

' '' ' ' '
numeros = [1, 2, 3, 4, 5]
cuadrados = [numero ** 2 for numero in numeros]

print(cuadrados)
