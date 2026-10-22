# Práctica 2.4 - Cambios de inventario (cada paso se muestra)
productos = ["Teclado", "Mouse", "Monitor"]
nuevos = ["Impresora", "Cámara"]

productos[productos.index("Mouse")] = "Mouse inalámbrico"
print("1. Reemplazar:", productos)

productos.insert(0, "Parlantes")
print("2. Insertar al inicio:", productos)

productos.extend(nuevos)
print("3. Extender:", productos)

productos.remove("Monitor")
print("4. Eliminar Monitor:", productos)

ultimo = productos.pop()
print("5. Extraer el último:", ultimo, "->", productos)

# Resultado final: ['Parlantes', 'Teclado', 'Mouse inalámbrico', 'Impresora']
