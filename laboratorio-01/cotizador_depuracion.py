# Reto de depuración (Práctica 1.5)
# Copia del cotizador con tres problemas provocados a propósito y su corrección.
# Cada bloque deja comentado el error original y la causa.

# --- Problema 1: error de sintaxis -----------------------------------------
# Original:   print("Subtotal: $" + str(subtotal)        <- faltaba el paréntesis final
# Mensaje:    SyntaxError: '(' was never closed (señala la línea del print)
# Corrección: cerrar el paréntesis.

# --- Problema 2: nombre de variable inexistente ----------------------------
# Original:   print("Total: $", totall)                  <- "totall" nunca se creó
# Mensaje:    NameError: name 'totall' is not defined
# Corrección: usar el nombre correcto: total.

# --- Problema 3: error lógico (se ejecuta pero da un resultado incorrecto) --
# Original:   valor_descuento = subtotal * descuento     <- faltaba dividir entre 100
#             Con descuento = 10 descontaba 10 veces el subtotal, no el 10 %.
# Corrección: valor_descuento = subtotal * (descuento / 100)

precio = 100000.0
cantidad = 2
descuento = 10  # porcentaje entero

subtotal = precio * cantidad
valor_descuento = subtotal * (descuento / 100)   # corrección del problema 3
total = subtotal - valor_descuento

print("Subtotal: $" + str(subtotal))               # corrección del problema 1
print("Total: $", total)                           # corrección del problema 2
