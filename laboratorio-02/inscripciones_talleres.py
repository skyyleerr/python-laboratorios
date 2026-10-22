python = {"Ana", "Carlos", "Laura", "Andrés", "Sofía"}
java = {"Laura", "Andrés", "Pedro", "Camila", "Ana"}

# 1. Inscritos en al menos uno de los talleres
print("Inscritos en al menos uno de los talleres:")
print(python | java)

# 2. Inscritos en ambos talleres
print("\nInscritos en ambos talleres:")
print(python & java)

# 3. Inscritos únicamente en Python
print("\nInscritos únicamente en Python:")
print(python - java)

# 4. Inscritos únicamente en Java
print("\nInscritos únicamente en Java:")
print(java - python)

# 5. Inscritos en uno solo de los talleres
print("\nInscritos en uno solo de los talleres:")
print(python ^ java)


# C:\Users\Asus\Downloads\python-laboratorio-02>C:\Users\Asus\AppData\Local\Programs\Python\Python315\python.exe c:/Users/Asus/Downloads/python-laboratorio-02/inscripciones_talleres.py

# Inscritos en al menos uno de los talleres:
# {'Laura', 'Carlos', 'Ana', 'Andrés', 'Camila', 'Sofía', 'Pedro'}

# Inscritos en ambos talleres:
# {'Ana', 'Laura', 'Andrés'}

# Inscritos únicamente en Python:
# {'Carlos', 'Sofía'}

# Inscritos únicamente en Java:
# {'Camila', 'Pedro'}

# Inscritos en uno solo de los talleres:
# {'Carlos', 'Sofía', 'Camila', 'Pedro'}