# Práctica 2.4 - Reemplazar, insertar y extraer
productos = ["Teclado", "Mouse", "Monitor"]

productos[1] = "Mouse inalámbrico"   # reemplaza
productos.insert(1, "Cámara web")    # inserta en la posición 1

eliminado = productos.pop()          # extrae el último

print("Elementos:", productos)
print("Extraído:", eliminado)

# Elementos: ['Teclado', 'Cámara web', 'Mouse inalámbrico']
# Extraído: Monitor
