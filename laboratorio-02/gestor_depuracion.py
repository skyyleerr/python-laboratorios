# Reto de depuración de la Práctica 2.9
# Cinco errores provocados a propósito sobre el gestor, con su causa y su corrección.
# (Fragmentos independientes; el gestor real está en gestor_inventario.py.)

# --- Error 1: la lista se recrea en cada vuelta del menú -------------------------
# Original:
#   while opcion != "0":
#       productos = []          <- dentro del ciclo
# Causa: cada vuelta crea una lista vacía y se pierden los productos registrados.
# Corrección: crear productos = [] UNA sola vez, antes del while.

# --- Error 2: clave inexistente --------------------------------------------------
# Original:   print(producto["stock"])        -> KeyError: 'stock'
# Causa: las claves del diccionario son codigo, nombre, categoria, precio y cantidad.
# Corrección: usar la clave correcta, producto["cantidad"], o producto.get("stock", 0).

# --- Error 3: código que duplica registros ---------------------------------------
# Original:   productos.append(nuevo_producto)   sin buscar antes el código
# Causa: no se recorría la lista para comprobar si el código ya existía.
# Corrección: recorrer productos y rechazar el registro si producto["codigo"] == codigo.

# --- Error 4: condición que permite cantidades negativas -------------------------
# Original:   if nueva_cantidad < -1:  ...       <- límite mal escrito
# Causa: la condición deja pasar -1 (y se confunde < con <=).
# Corrección: if nueva_cantidad < 0: rechazar y conservar la cantidad anterior.

# --- Error 5: total que suma precios sin multiplicar por cantidades --------------
# Original:   valor_total = sum(p["precio"] for p in productos)
# Causa: faltaba multiplicar precio * cantidad. Con P001-P003 daba 830000.0 en vez de 1740000.0.
# Corrección: sum(p["precio"] * p["cantidad"] for p in productos)

productos = [
    {"codigo": "P001", "nombre": "Teclado", "categoria": "Periféricos", "precio": 85000.0, "cantidad": 4},
    {"codigo": "P002", "nombre": "Mouse", "categoria": "Periféricos", "precio": 45000.0, "cantidad": 0},
    {"codigo": "P003", "nombre": "Disco SSD", "categoria": "Componentes", "precio": 700000.0, "cantidad": 2},
]

valor_incorrecto = sum(p["precio"] for p in productos)
valor_correcto = sum(p["precio"] * p["cantidad"] for p in productos)

print("Total incorrecto (sin cantidad):", valor_incorrecto)
print("Total correcto (precio * cantidad):", valor_correcto)
print("Cantidad del primer producto:", productos[0].get("stock", productos[0]["cantidad"]))
