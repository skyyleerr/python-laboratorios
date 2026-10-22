notas = [2.5, 3.0, 4.8, 1.9, 3.7, 5.0]

# 1. Notas aprobadas: 3.0 o más
notas_aprobadas = [nota for nota in notas if nota >= 3.0]

# 2. Notas inferiores a 3.0
notas_reprobadas = [nota for nota in notas if nota < 3.0]

# 3. Todas las notas multiplicadas por 2
notas_duplicadas = [nota * 2 for nota in notas]

# Mostrar los resultados
print("Notas aprobadas:", notas_aprobadas)
print("Notas inferiores a 3.0:", notas_reprobadas)
print("Notas multiplicadas por 2:", notas_duplicadas)

# C:\Users\Asus\Downloads\python-laboratorio-02>C:\Users\Asus\AppData\Local\Programs\Python\Python315\python.exe c:/Users/Asus/Downloads/python-laboratorio-02/notas_aprobadas.py
# Notas aprobadas: [3.0, 4.8, 3.7, 5.0]
# Notas inferiores a 3.0: [2.5, 1.9]
# Notas multiplicadas por 2: [5.0, 6.0, 9.6, 3.8, 7.4, 10.0]