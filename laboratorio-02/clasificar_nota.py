nota = float(input("Nota: "))

if nota >= 4.5:
    print("Desempeño sobresaliente")
elif nota >= 4.0:
    print("Desempeño alto")
elif nota >= 3.0:
    print("Aprobado")
else:
    print("No aprobado")
    
# PS C:\Users\ProgacionSena\Desktop\python-laboratorio-02> python clasificar_nota.py
# Nota: 4.8
# Desempeño sobresaliente

# PS C:\Users\ProgacionSena\Desktop\python-laboratorio-02> python clasificar_nota.py
# Nota: 4.2
# Desempeño alto

# PS C:\Users\ProgacionSena\Desktop\python-laboratorio-02> python clasificar_nota.py
# Nota: 3.0
# Aprobado

# PS C:\Users\ProgacionSena\Desktop\python-laboratorio-02> python clasificar_nota.py
# Nota: 2.9
# No aprobado

nota = float(input("Nota: "))

if nota >= 3.0:
    print("Aprobado")
elif nota >= 4.5:
    print("Desempeño sobresaliente")
elif nota >= 4.0:
    print("Desempeño alto")
  
# PS C:\Users\ProgacionSena\Desktop\python-laboratorio-02> python clasificar_nota.py    
# Nota: 4.8
# Aprobado