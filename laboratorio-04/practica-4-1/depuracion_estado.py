def actualizar_cantidad(producto, nueva_cantidad):
    # Validar antes de cambiar el estado.
    if isinstance(nueva_cantidad, bool) or not isinstance(nueva_cantidad, int):
        raise TypeError("La cantidad debe ser entera.")
    if nueva_cantidad < 0:
        raise ValueError("La cantidad no puede ser negativa.")
    producto["cantidad"] = nueva_cantidad
    return True

producto = {"codigo": "P001", "cantidad": 4}
try:
    actualizar_cantidad(producto, -1)
except ValueError as error:
    print(error)
print("Cantidad conservada:", producto["cantidad"])
