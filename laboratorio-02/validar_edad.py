edad = int(input("Edad: "))

if edad >= 18:
    print("Es mayor de edad.")

print("Fin del programa.")

# PS C:\Users\ProgacionSena\Desktop\python-laboratorio-02> python validar_edad.py
# Edad: 16
# Fin del programa.

# PS C:\Users\ProgacionSena\Desktop\python-laboratorio-02> python validar_edad.py
# Edad: 21
# Es mayor de edad.
# Fin del programa.

''''''

edad = int(input("Edad: "))

if edad >= 18:
    print("Es mayor de edad.")
else:
    print("Es menor de edad.")
    
# PS C:\Users\ProgacionSena\Desktop\python-laboratorio-02> python validar_edad.py
# Edad: 17
# Es menor de edad.

# PS C:\Users\ProgacionSena\Desktop\python-laboratorio-02> python validar_edad.py
# Edad: 18
# Es mayor de edad.

# PS C:\Users\ProgacionSena\Desktop\python-laboratorio-02> python validar_edad.py
# Edad: 25
# Es mayor de edad.