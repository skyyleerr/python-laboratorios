# Práctica 2.2 - Operador and
# Puede ingresar solo si está inscrito Y tiene el documento requerido.
# Se prueban las cuatro combinaciones de True y False.

combinaciones = [(True, True), (True, False), (False, True), (False, False)]

for esta_inscrito, tiene_documento in combinaciones:
    if esta_inscrito and tiene_documento:
        resultado = "Puede ingresar."
    else:
        resultado = "No cumple todos los requisitos."
    print(f"inscrito={esta_inscrito}, documento={tiene_documento} -> {resultado}")

# inscrito=True, documento=True -> Puede ingresar.
# inscrito=True, documento=False -> No cumple todos los requisitos.
# inscrito=False, documento=True -> No cumple todos los requisitos.
# inscrito=False, documento=False -> No cumple todos los requisitos.
