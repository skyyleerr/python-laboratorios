grupo_a = {"Ana", "Carlos", "Laura", "Sara"}
grupo_b = {"Laura", "Sara", "David", "Pablo"}

print("Unión:", grupo_a | grupo_b)
print("Intersección:", grupo_a & grupo_b)
print("Solo A:", grupo_a - grupo_b)
print("Diferencia simétrica:", grupo_a ^ grupo_b)

# C:\Users\Asus\Downloads\python-laboratorio-02>C:\Users\Asus\AppData\Local\Programs\Python\Python315\python.exe c:/Users/Asus/Downloads/python-laboratorio-02/operaciones_conjuntos.py
# Unión: {'Pablo', 'Sara', 'Carlos', 'Laura', 'Ana', 'David'}
# Intersección: {'Sara', 'Laura'}
# Solo A: {'Ana', 'Carlos'}
# Diferencia simétrica: {'Pablo', 'Carlos', 'Ana', 'David'}