precios = [10000, 20000, 50000, 80000]

# Primera forma: for y append()
precios_con_impuesto = []

for precio in precios:
    precio_final = precio * 1.19
    precios_con_impuesto.append(precio_final)

print("Precios con for y append():")
print(precios_con_impuesto)

# Segunda forma: comprensión de listas
precios_comprension = [precio * 1.19 for precio in precios]

print("\nPrecios con comprensión:")
print(precios_comprension)

# Comprobar que los resultados son equivalentes
print("\n¿Los resultados son equivalentes?")
print(precios_con_impuesto == precios_comprension)

# C:\Users\Asus\Downloads\python-laboratorio-02>C:\Users\Asus\AppData\Local\Programs\Python\Python315\python.exe c:/Users/Asus/Downloads/python-laboratorio-02/precios_con_impuesto.py
# Precios con for y append():
# [11900.0, 23800.0, 59500.0, 95200.0]

# Precios con comprensión:
# [11900.0, 23800.0, 59500.0, 95200.0]

# ¿Los resultados son equivalentes?
# True