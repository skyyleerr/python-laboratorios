materias = ["Python", "Bases de datos", "Java", "HTML", "CSS"]

print("Lista de materias:")

for i in range(len(materias)):
    print(f"{i + 1}. {materias[i]}")

# Agregar una nueva materia
materias.append("JavaScript")

print("\nLista actualizada:")

for i in range(len(materias)):
    print(f"{i + 1}. {materias[i]}")

# C:\Users\Asus\Downloads\python-laboratorio-02>C:\Users\Asus\AppData\Local\Programs\Python\Python315\python.exe c:/Users/Asus/Downloads/python-laboratorio-02/lista_materias.py
# Lista de materias:
# 1. Python
# 2. Bases de datos
# 3. Java
# 4. HTML
# 5. CSS

# Lista actualizada:
# 1. Python
# 2. Bases de datos
# 3. Java
# 4. HTML
# 5. CSS
# 6. JavaScript