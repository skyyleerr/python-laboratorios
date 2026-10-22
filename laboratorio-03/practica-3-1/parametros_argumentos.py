def saludar(nombre):
    print(f"Hola, {nombre}")


def mostrar_producto(nombre, cantidad):
    print(f"Producto: {nombre}")
    print(f"Existencias: {cantidad}")


def presentar(nombre, ciudad):
    print(f"{nombre} vive en {ciudad}")


saludar("Laura")
saludar("Andrés")
mostrar_producto("Teclado", 4)
mostrar_producto("Mouse", 7)

presentar("Ana", "Bogotá")
# Esta llamada con el orden del enunciado no produce error, sino una frase extraña:
# presentar("Cali", "Luis") imprime: Cali vive en Luis.
# Corrección: presentar("Luis", "Cali")
presentar("Luis", "Cali")
