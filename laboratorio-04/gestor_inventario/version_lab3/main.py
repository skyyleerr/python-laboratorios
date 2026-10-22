"""Interacción por consola del gestor: aquí se usa input() y se muestran mensajes."""

import math

from inventario import Inventario
from producto import Producto

# Producto:
#   representa un artículo y controla sus valores
#
# Inventario:
#   conserva varios objetos Producto
#   registra, busca, actualiza, elimina y consulta
#
# main:
#   solicita datos
#   muestra menú
#   informa los resultados


def mostrar_menu():
    print()
    print("================================")
    print("       GESTOR DE INVENTARIO")
    print("================================")
    print("1. Registrar producto")
    print("2. Listar productos")
    print("3. Buscar por código")
    print("4. Actualizar existencias")
    print("5. Eliminar producto")
    print("6. Consultar productos sin stock")
    print("7. Resumen del inventario")
    print("0. Salir")


def leer_texto(mensaje):
    while True:
        texto = input(mensaje).strip()
        if texto:
            return texto
        print("Este campo no puede estar vacío.")


def convertir_precio(texto):
    """Convierte montos locales: 85.000, 85.000,50 o 85000.50."""
    texto = texto.strip().replace("$", "").replace(" ", "")
    if "," in texto:
        texto = texto.replace(".", "").replace(",", ".")
    elif "." in texto:
        partes = texto.split(".")
        if len(partes) > 2 or (len(partes) == 2 and len(partes[1]) == 3):
            texto = texto.replace(".", "")
    return float(texto)


def leer_precio():
    while True:
        try:
            precio = convertir_precio(input("Precio: "))
        except ValueError:
            print("Debes escribir un número válido.")
            continue
        if not math.isfinite(precio):
            print("El precio debe ser un número finito.")
            continue
        if precio <= 0:
            print("El precio debe ser mayor que cero.")
            continue
        return precio


def leer_cantidad():
    while True:
        try:
            cantidad = int(input("Cantidad: "))
        except ValueError:
            print("Debes escribir un número entero.")
            continue
        if cantidad < 0:
            print("La cantidad no puede ser negativa.")
            continue
        return cantidad


def mostrar_producto(producto):
    print(producto)


def registrar_producto(inventario):
    codigo = leer_texto("Código: ")
    nombre = leer_texto("Nombre: ")
    categoria = leer_texto("Categoría: ")
    precio = leer_precio()
    cantidad = leer_cantidad()

    try:
        producto = Producto(codigo, nombre, categoria, precio, cantidad)
    except ValueError as error:
        print("No se pudo registrar el producto:", error)
        return

    if inventario.registrar_producto(producto):
        print("Producto registrado.")
    else:
        print("No se pudo registrar: el código ya existe.")


def listar_productos(inventario):
    productos = inventario.listar_productos()
    if not productos:
        print("El inventario está vacío.")
        return
    for producto in productos:
        mostrar_producto(producto)


def buscar_producto(inventario):
    codigo = leer_texto("Código: ")
    producto = inventario.buscar_por_codigo(codigo)
    if producto is None:
        print("Producto no registrado.")
    else:
        mostrar_producto(producto)


def actualizar_existencias(inventario):
    codigo = leer_texto("Código: ")
    producto = inventario.buscar_por_codigo(codigo)
    if producto is None:
        print("Producto no registrado.")
        return
    cantidad = leer_cantidad()
    if inventario.actualizar_existencias(codigo, cantidad):
        print("Existencias actualizadas.")
    else:
        print("No se pudieron actualizar las existencias.")


def eliminar_producto(inventario):
    codigo = leer_texto("Código: ")
    if inventario.eliminar_producto(codigo):
        print("Producto eliminado.")
    else:
        print("Producto no registrado; no se eliminó nada.")


def mostrar_productos_sin_stock(inventario):
    productos = inventario.productos_sin_stock()
    if not productos:
        print("No hay productos sin stock.")
        return
    print("Sin existencias:")
    for producto in productos:
        print("-", producto.nombre)


def mostrar_resumen(inventario):
    resumen = inventario.resumen()
    print("Productos registrados:", resumen["productos_registrados"])
    print("Unidades disponibles:", resumen["unidades_disponibles"])
    print("Valor del inventario: $" + str(resumen["valor_total"]))
    categorias = sorted(resumen["categorias"])
    texto_categorias = ", ".join(categorias) if categorias else "ninguna"
    print("Categorías utilizadas:", texto_categorias)
    print("Cantidad de categorías:", len(categorias))


def main():
    inventario = Inventario()
    while True:
        mostrar_menu()
        opcion = input("Opción: ").strip()

        if opcion == "1":
            registrar_producto(inventario)
        elif opcion == "2":
            listar_productos(inventario)
        elif opcion == "3":
            buscar_producto(inventario)
        elif opcion == "4":
            actualizar_existencias(inventario)
        elif opcion == "5":
            eliminar_producto(inventario)
        elif opcion == "6":
            mostrar_productos_sin_stock(inventario)
        elif opcion == "7":
            mostrar_resumen(inventario)
        elif opcion == "0":
            print("Programa finalizado.")
            break
        else:
            print("Opción no válida.")


if __name__ == "__main__":
    main()
