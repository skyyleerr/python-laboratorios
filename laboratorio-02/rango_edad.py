edad = int(input("Edad: "))

if edad >= 18 and edad <= 65:
    print("La edad está dentro del rango.")
else:
    print("La edad está fuera del rango.")
    
# PS C:\Users\ProgacionSena\Desktop\python-laboratorio-02> python rango_edad.py
# Edad: 17
# La edad está fuera del rango.
# PS C:\Users\ProgacionSena\Desktop\python-laboratorio-02> python rango_edad.py
# Edad: 18
# La edad está dentro del rango.
# PS C:\Users\ProgacionSena\Desktop\python-laboratorio-02> python rango_edad.py
# Edad: 65
# La edad está dentro del rango.
# PS C:\Users\ProgacionSena\Desktop\python-laboratorio-02> python rango_edad.py
# Edad: 66
# La edad está fuera del rango.