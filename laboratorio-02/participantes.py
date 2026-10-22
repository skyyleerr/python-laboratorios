grupo_a = ["Ana", "Carlos", "Laura", "Sara"]
grupo_b = ["Laura", "Pedro", "Ana", "Sofia"]

# Unir las dos listas y convertirlas en un conjunto
participantes = set(grupo_a + grupo_b)

# Mostrar los participantes únicos
print("Participantes únicos:", participantes)
print("Cantidad de personas diferentes:", len(participantes))

# Agregar una persona
participantes.add("Andrés")
print("Después de agregar a Andrés:", participantes)

# Eliminar una persona
participantes.discard("Carlos")
print("Después de eliminar a Carlos:", participantes)
