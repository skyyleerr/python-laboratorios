categorias = ("Periféricos", "Componentes", "Accesorios", "Monitores")

# Mostrar las categorías numeradas
print("Categorías disponibles:")

for numero, categoria in enumerate(categorias, start=1):
    print(numero, "-", categoria)

# Solicitar una categoría
elegida = input("Escribe una categoría: ").strip()

# Verificar si la categoría existe
if elegida in categorias:
    print("Categoría válida.")
else:
    print("Categoría no registrada.")

# Mostrar la cantidad de categorías
print("Cantidad de categorías:", len(categorias))

######

# C:\Users\Asus\Downloads\python-laboratorio-02>C:\Users\Asus\AppData\Local\Programs\Python\Python315\python.exe c:/Users/Asus/Downloads/python-laboratorio-02/categorias_tupla.py
# Categorías disponibles:
# 1 - Periféricos
# 2 - Componentes
# 3 - Accesorios
# 4 - Monitores
# Escribe una categoría: Componentes
# Categoría válida.
# Cantidad de categorías: 4

# C:\Users\Asus\Downloads\python-laboratorio-02>C:\Users\Asus\AppData\Local\Programs\Python\Python315\python.exe c:/Users/Asus/Downloads/python-laboratorio-02/categorias_tupla.py
# Categorías disponibles:
# 1 - Periféricos
# 2 - Componentes
# 3 - Accesorios
# 4 - Monitores
# Escribe una categoría: Celulares
# Categoría no registrada.
# Cantidad de categorías: 4

# C:\Users\Asus\Downloads\python-laboratorio-02>C:\Users\Asus\AppData\Local\Programs\Python\Python315\python.exe c:/Users/Asus/Downloads/python-laboratorio-02/categorias_tupla.py
# Categorías disponibles:
# 1 - Periféricos
# 2 - Componentes
# 3 - Accesorios
# 4 - Monitores
# Escribe una categoría: Monitore
# Categoría no registrada.
# Cantidad de categorías: 4
######