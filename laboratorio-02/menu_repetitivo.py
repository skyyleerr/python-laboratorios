opcion = ""

while opcion != "0":
    print()
    print("1. Saludar")
    print("2. Mostrar mensaje")
    print("0. Salir")

    opcion = input("Opción: ").strip()

    if opcion == "1":
        print("Hola.")
    elif opcion == "2":
        print("El programa sigue ejecutándose.")
    elif opcion == "0":
        print("Programa terminado.")
    else:
        print("Opción no válida.")

# C:\Users\Asus\Downloads\python-laboratorio-02>C:\Users\Asus\AppData\Local\Programs\Python\Python315\python.exe c:/Users/Asus/Downloads/python-laboratorio-02/menu_repetitivo.py

# 1. Saludar
# 2. Mostrar mensaje
# 0. Salir
# Opción: 1
# Hola.

# 1. Saludar
# 2. Mostrar mensaje
# 0. Salir
# Opción: 2
# El programa sigue ejecutándose.

# 1. Saludar
# 2. Mostrar mensaje
# 0. Salir
# Opción: 9
# Opción no válida.

# 1. Saludar
# 2. Mostrar mensaje
# 0. Salir
# Opción: 0
# Programa terminado.