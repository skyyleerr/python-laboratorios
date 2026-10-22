# Reto de ampliación de la Práctica 2.9 (opciones 8 a 12 añadidas al gestor original)
# Lista de diccionarios para almacenar los productos
# Tupla de categorías válidas
# Ciclo del menú
#   Registrar
#   Listar
#   Buscar
#   Actualizar
#   Eliminar
#   Filtrar sin stock
#   Mostrar resumen

CATEGORIAS = ("Periféricos", "Componentes", "Accesorios")

productos = []
opcion = ""

while opcion != "0":
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
    print("8. Aumentar o disminuir existencias")
    print("9. Listar ordenado por nombre")
    print("10. Diccionario código -> nombre")
    print("11. Buscar por categoría")
    print("12. Producto de mayor valor")
    print("0. Salir")

    opcion = input("Opción: ").strip()

    # 1. Registrar producto
    if opcion == "1":
        codigo = input("Código: ").strip().upper()
        nombre = input("Nombre: ").strip()
        categoria = input("Categoría: ").strip()
        
        if codigo == "" or nombre == "" or categoria == "":
            print("Error: los campos de texto no pueden estar vacíos.")

        elif categoria not in CATEGORIAS:
            print("Error: categoría no válida.")
            print("Categorías permitidas:", CATEGORIAS)

        else:
            encontrado = None

            for producto in productos:
                if producto["codigo"] == codigo:
                    encontrado = producto
                    break

            if encontrado is not None:
                print("Error: ya existe un producto con ese código.")

            else:
                precio = float(input("Precio: "))
                cantidad = int(input("Cantidad: "))

                if precio <= 0:
                    print("Error: el precio debe ser mayor que cero.")

                elif cantidad < 0:
                    print("Error: la cantidad no puede ser negativa.")

                else:
                    nuevo_producto = {
                        "codigo": codigo,
                        "nombre": nombre,
                        "categoria": categoria,
                        "precio": precio,
                        "cantidad": cantidad
                    }

                    productos.append(nuevo_producto)
                    print("Producto registrado.")

    # 2. Listar productos
    elif opcion == "2":
        if len(productos) == 0:
            print("No hay productos registrados.")

        else:
            print("\nLISTA DE PRODUCTOS")

            for producto in productos:
                print(
                    f'{producto["codigo"]} - {producto["nombre"]} - '
                    f'{producto["categoria"]} - ${producto["precio"]} - '
                    f'{producto["cantidad"]} unidades'
                )

    # 3. Buscar por código
    elif opcion == "3":
        codigo_buscado = input("Código del producto: ").strip().upper()
        encontrado = None

        for producto in productos:
            if producto["codigo"] == codigo_buscado:
                encontrado = producto
                break

        if encontrado is not None:
            print("\nPRODUCTO ENCONTRADO")
            print("Código:", encontrado["codigo"])
            print("Nombre:", encontrado["nombre"])
            print("Categoría:", encontrado["categoria"])
            print(f"Precio: ${encontrado['precio']}")
            print("Cantidad:", encontrado["cantidad"])
        else:
            print("El producto no existe.")

    # 4. Actualizar existencias
    elif opcion == "4":
        codigo_buscado = input("Código del producto: ").strip().upper()
        encontrado = None

        for producto in productos:
            if producto["codigo"] == codigo_buscado:
                encontrado = producto
                break

        if encontrado is None:
            print("El producto no existe.")

        else:
            nueva_cantidad = int(input("Nueva cantidad: "))

            if nueva_cantidad < 0:
                print("Error: la cantidad no puede ser negativa.")
                print("Se conserva la cantidad anterior.")

            else:
                encontrado["cantidad"] = nueva_cantidad
                print("Existencias actualizadas.")

    # 5. Eliminar producto
    elif opcion == "5":
        codigo_buscado = input("Código del producto: ").strip().upper()
        encontrado = None

        for producto in productos:
            if producto["codigo"] == codigo_buscado:
                encontrado = producto
                break

        if encontrado is not None:
            productos.remove(encontrado)
            print("Producto eliminado.")
        else:
            print("El producto no existe.")

    # 6. Consultar productos sin stock
    elif opcion == "6":
        agotados = [
            producto["nombre"]
            for producto in productos
            if producto["cantidad"] == 0
        ]

        if len(agotados) == 0:
            print("No hay productos sin existencias.")

        else:
            print("Sin existencias:")

            for nombre_producto in agotados:
                print("-", nombre_producto)

    # 7. Resumen del inventario
    elif opcion == "7":
        cantidad_productos = len(productos)

        unidades_totales = sum(
            producto["cantidad"]
            for producto in productos
        )

        valor_total = sum(
            producto["precio"] * producto["cantidad"]
            for producto in productos
        )

        categorias_utilizadas = {
            producto["categoria"]
            for producto in productos
        }

        print("\nRESUMEN DEL INVENTARIO")
        print("Productos:", cantidad_productos)
        print("Unidades:", unidades_totales)
        print(f"Valor del inventario: ${valor_total}")
        print("Categorías utilizadas:", ", ".join(sorted(categorias_utilizadas)))

    # 8. Movimiento de existencias (aumentar o disminuir)
    elif opcion == "8":
        codigo_buscado = input("Código del producto: ").strip().upper()
        encontrado = None

        for producto in productos:
            if producto["codigo"] == codigo_buscado:
                encontrado = producto
                break

        if encontrado is None:
            print("El producto no existe.")
        else:
            movimiento = int(input("Movimiento (+ aumenta, - disminuye): "))

            if encontrado["cantidad"] + movimiento < 0:
                print("Error: las existencias no pueden quedar negativas.")
            else:
                encontrado["cantidad"] += movimiento
                print("Existencias actuales:", encontrado["cantidad"])

    # 9. Ordenado por nombre sin cambiar la lista original (sorted)
    elif opcion == "9":
        for producto in sorted(productos, key=lambda p: p["nombre"].lower()):
            print(f'{producto["nombre"]} - {producto["codigo"]}')

    # 10. Diccionario código -> nombre mediante comprensión
    elif opcion == "10":
        catalogo = {producto["codigo"]: producto["nombre"] for producto in productos}
        print(catalogo)

    # 11. Buscar por categoría
    elif opcion == "11":
        categoria_buscada = input("Categoría: ").strip()
        coincidencias = [p["nombre"] for p in productos if p["categoria"] == categoria_buscada]
        if len(coincidencias) == 0:
            print("No hay productos en esa categoría.")
        else:
            print("Productos:", ", ".join(coincidencias))

    # 12. Producto con mayor valor de inventario (precio * cantidad)
    elif opcion == "12":
        if len(productos) == 0:
            print("No hay productos registrados.")
        else:
            mayor = max(productos, key=lambda p: p["precio"] * p["cantidad"])
            print(f'Mayor valor: {mayor["nombre"]} (${mayor["precio"] * mayor["cantidad"]})')

    # Salir
    elif opcion == "0":
        print("Programa finalizado.")

    else:
        print("Opción no válida.")

# C:\Users\Asus\Downloads\python-laboratorio-02>C:\Users\Asus\AppData\Local\Programs\Python\Python315\python.exe "c:/Users/Asus/Downloads/python-laboratorio-02/Práctica 2.9/gestor_inventario.py"

# ================================
#        GESTOR DE INVENTARIO
# ================================
# 1. Registrar producto
# 2. Listar productos
# 3. Buscar por código
# 4. Actualizar existencias
# 5. Eliminar producto
# 6. Consultar productos sin stock
# 7. Resumen del inventario
# 0. Salir
# Opción: 1
# Código: P001
# Nombre: Teclado
# Categoría: Periféricos
# Precio: 85.000
# Cantidad: 4
# Producto registrado.

# ================================
#        GESTOR DE INVENTARIO
# ================================
# 1. Registrar producto
# 2. Listar productos
# 3. Buscar por código
# 4. Actualizar existencias
# 5. Eliminar producto
# 6. Consultar productos sin stock
# 7. Resumen del inventario
# 0. Salir
# Opción: 1
# Código: P002
# Nombre: Mouse
# Categoría: Periféricos
# Precio: 45.000
# Cantidad: 0
# Producto registrado.

# ================================
#        GESTOR DE INVENTARIO
# ================================
# 1. Registrar producto
# 2. Listar productos
# 3. Buscar por código
# 4. Actualizar existencias
# 5. Eliminar producto
# 6. Consultar productos sin stock
# 7. Resumen del inventario
# 0. Salir
# Opción: 1
# Código: P003
# Nombre: Disco SSD
# Categoría: Componentes
# Precio: 700.000
# Cantidad: 2
# Producto registrado.

# ================================
#        GESTOR DE INVENTARIO
# ================================
# 1. Registrar producto
# 2. Listar productos
# 3. Buscar por código
# 4. Actualizar existencias
# 5. Eliminar producto
# 6. Consultar productos sin stock
# 7. Resumen del inventario
# 0. Salir
# Opción: 6
# Sin existencias:
# - Mouse

# ================================
#        GESTOR DE INVENTARIO
# ================================
# 1. Registrar producto
# 2. Listar productos
# 3. Buscar por código
# 4. Actualizar existencias
# 5. Eliminar producto
# 6. Consultar productos sin stock
# 7. Resumen del inventario
# 0. Salir
# Opción: 7

# RESUMEN DEL INVENTARIO
# Productos: 3
# Unidades: 6
# Valor total del inventario: $ 1740.0
# Categorías utilizadas: {'Componentes', 'Periféricos'}