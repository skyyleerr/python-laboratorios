libros = [
    {
        "codigo": "L001",
        "titulo": "Cien años de soledad",
        "autor": "Gabriel García Márquez",
        "anio": 1967
    },
    {
        "codigo": "L002",
        "titulo": "El principito",
        "autor": "Antoine de Saint-Exupéry",
        "anio": 1943
    },
    {
        "codigo": "L003",
        "titulo": "1984",
        "autor": "George Orwell",
        "anio": 1949
    }
]

# Buscar un libro por código
codigo_buscado = input("Ingrese el código del libro que desea buscar: ").strip().upper()

encontrado = False

for libro in libros:
    if libro["codigo"] == codigo_buscado:
        print("\nLibro encontrado:")
        for clave, valor in libro.items():
            print(clave, ":", valor)

        encontrado = True
        break

if not encontrado:
    print("El libro no fue localizado.")

# Registrar un nuevo libro
print("\n--- Registrar un nuevo libro ---")

nuevo_codigo = input("Código: ").strip().upper()

codigo_repetido = False

for libro in libros:
    if libro["codigo"] == nuevo_codigo:
        codigo_repetido = True
        break

if codigo_repetido:
    print("Error: ya existe un libro con ese código.")
else:
    titulo = input("Título: ").strip()
    autor = input("Autor: ").strip()
    anio = int(input("Año de publicación: "))

    nuevo_libro = {
        "codigo": nuevo_codigo,
        "titulo": titulo,
        "autor": autor,
        "anio": anio
    }

    libros.append(nuevo_libro)
    print("Libro agregado correctamente.")

# Mostrar el catálogo actualizado
print("\n--- Catálogo de libros ---")

for libro in libros:
    print("-------------------------")
    for clave, valor in libro.items():
        print(clave, ":", valor)

# C:\Users\Asus\Downloads\python-laboratorio-02>C:\Users\Asus\AppData\Local\Programs\Python\Python315\python.exe c:/Users/Asus/Downloads/python-laboratorio-02/catalogo_libros.py
# Ingrese el código del libro que desea buscar: L001

# Libro encontrado:
# codigo : L001
# titulo : Cien años de soledad
# autor : Gabriel García Márquez
# anio : 1967

# --- Registrar un nuevo libro ---
# Código: L002
# Error: ya existe un libro con ese código.

# --- Catálogo de libros ---
# -------------------------
# codigo : L001
# titulo : Cien años de soledad
# autor : Gabriel García Márquez
# anio : 1967
# -------------------------
# codigo : L002
# titulo : El principito
# autor : Antoine de Saint-Exupéry
# anio : 1943
# -------------------------
# codigo : L003
# titulo : 1984
# autor : George Orwell
# anio : 1949