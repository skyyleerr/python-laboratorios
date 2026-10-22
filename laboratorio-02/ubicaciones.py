# Registrar tres ubicaciones con latitud y longitud
ubicacion1 = (4.6097, -74.0817)
ubicacion2 = (6.2442, -75.5812)
ubicacion3 = (3.4516, -76.5320)

# Desempaquetar las coordenadas
latitud1, longitud1 = ubicacion1
latitud2, longitud2 = ubicacion2
latitud3, longitud3 = ubicacion3

# Mostrar las ubicaciones
print("Ubicación 1:")
print("Latitud:", latitud1)
print("Longitud:", longitud1)

print("Ubicación 2:")
print("Latitud:", latitud2)
print("Longitud:", longitud2)

print("Ubicación 3:")
print("Latitud:", latitud3)
print("Longitud:", longitud3)

# Datos de una sede
sede = ("S001", "Sede principal", "Bogotá")

# Desempaquetar los datos de la sede
codigo, nombre, ciudad = sede

# Mostrar los datos
print("Código:", codigo)
print("Nombre:", nombre)
print("Ciudad:", ciudad)

# C:\Users\Asus\Downloads\python-laboratorio-02>python ubicaciones.py
# Ubicación 1:
# Latitud: 4.6097
# Longitud: -74.0817
# Ubicación 2:
# Latitud: 6.2442
# Longitud: -75.5812
# Ubicación 3:
# Latitud: 3.4516
# Longitud: -76.532
# Código: S001
# Nombre: Sede principal
# Ciudad: Bogotá