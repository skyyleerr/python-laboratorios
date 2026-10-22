respuesta = input("Escribe SI para continuar: ")

if respuesta == "SI":
    print("Continuando...")
else:
    print("Respuesta diferente de SI.")
    
# PS C:\Users\ProgacionSena\Desktop\python-laboratorio-02> python comparar_texto.py
# Escribe SI para continuar: SI
# Continuando...
# PS C:\Users\ProgacionSena\Desktop\python-laboratorio-02>  python comparar_texto.py
# Escribe SI para continuar: si
# Respuesta diferente de SI.
# PS C:\Users\ProgacionSena\Desktop\python-laboratorio-02> python comparar_texto.py
# Escribe SI para continuar: Si
# Respuesta diferente de SI.

respuesta = input("Escribe SI para continuar: ").strip().lower()

if respuesta == "si":
    print("Continuando...")
else:
    print("Respuesta diferente de SI.")