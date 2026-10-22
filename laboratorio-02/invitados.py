invitados = []

for i in range(5):
    nombre = input("Ingresa el nombre del invitado: ").strip()
    invitados.append(nombre)

print("Cantidad de invitados:", len(invitados))
print("Lista de invitados:", invitados)

# C:\Users\Asus\Downloads\python-laboratorio-02>C:\Users\Asus\AppData\Local\Programs\Python\Python315\python.exe c:/Users/Asus/Downloads/python-laboratorio-02/invitados.py
# Ingresa el nombre del invitado: Isaac
# Ingresa el nombre del invitado: Anthony
# Ingresa el nombre del invitado: Juan
# Ingresa el nombre del invitado: Cristian
# Ingresa el nombre del invitado: Molly
# Cantidad de invitados: 5
# Lista de invitados: ['Isaac', 'Anthony', 'Juan', 'Cristian', 'Molly']