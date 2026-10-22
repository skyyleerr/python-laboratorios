# Práctica 2.4 - Evitar duplicados
productos = ["Teclado", "Mouse"]

nombre = input("Producto nuevo: ").strip()

if nombre == "":
    print("El nombre no puede estar vacío.")
elif nombre in productos:
    print("El producto está repetido.")
else:
    productos.append(nombre)
    print("Producto agregado.")

print(productos)
