
edad = int(input("Ingresa tu edad: "))
inscripcion = input("¿Estás inscrito? (si/no): ").strip().lower()
documentos = int(input("Número de documentos entregados: "))

cumple_todo = edad >= 16 and inscripcion == "si" and documentos >= 3

if edad < 16:
    print("Falta cumplir la edad mínima de 16 años.")

if inscripcion != "si":
    print("La persona debe estar inscrita.")

if documentos < 3:
    print("Faltan documentos por entregar.")

if cumple_todo:
    print("La solicitud cumple todos los requisitos.")
else:
    print("La solicitud no cumple todos los requisitos.")

# ¿Cuál es la diferencia entre and y or?
# - and: todas las condiciones deben ser verdaderas. Ejemplo: tener la edad requerida y estar inscrito.
# - or: basta con que una condición sea verdadera. Ejemplo: aceptar un pago con tarjeta o en efectivo.

# ¿Por qué validar antes de calcular?
# Porque permite detectar datos incorrectos y evitar resultados que no tengan sentido. Por ejemplo, no deberíamos calcular el costo de una compra si la cantidad de productos es negativa.