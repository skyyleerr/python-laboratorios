import json
from pathlib import Path
base = Path(__file__).resolve().parent
ruta = base / "libros.json"
libros = [
    {"codigo": "L001", "titulo": "Cien años de soledad", "autor": "Gabriel García Márquez", "anio": 1967},
    {"codigo": "L002", "titulo": "Frankenstein", "autor": "Mary Shelley", "anio": 1818},
    {"codigo": "L003", "titulo": "La ciudad y los perros", "autor": "Mario Vargas Llosa", "anio": 1963},
]
with ruta.open("w", encoding="utf-8") as archivo:
    json.dump(libros, archivo, ensure_ascii=False, indent=2)
with ruta.open(encoding="utf-8") as archivo:
    recuperados = json.load(archivo)
for libro in recuperados:
    print(libro["codigo"], libro["titulo"], "—", libro["autor"], "(", libro["anio"], ")")
