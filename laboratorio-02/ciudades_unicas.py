ciudades = ["Bogotá", "Cali", "Bogotá", "Medellín", "Cali"]

unicas = set(ciudades)

print("Total de registros:", len(ciudades))
print("Ciudades diferentes:", len(unicas))
print(unicas)

lista_unicas = list(unicas)

print(lista_unicas)

# C:\Users\Asus\Downloads\python-laboratorio-02>C:\Users\Asus\AppData\Local\Programs\Python\Python315\python.exe c:/Users/Asus/Downloads/python-laboratorio-02/ciudades_unicas.py
# Total de registros: 5
# Ciudades diferentes: 3
# {'Medellín', 'Bogotá', 'Cali'}
# ['Medellín', 'Bogotá', 'Cali']