codigos = [" p001 ", "P002", "", " p003", "  "]

codigos_normalizados = [
    codigo.strip().upper()
    for codigo in codigos
    if codigo.strip() != ""
]

print("Códigos normalizados:", codigos_normalizados)

# C:\Users\Asus\Downloads\python-laboratorio-02>C:\Users\Asus\AppData\Local\Programs\Python\Python315\python.exe c:/Users/Asus/Downloads/python-laboratorio-02/normalizar_codigos.py
# Códigos normalizados: ['P001', 'P002', 'P003']