def duplicar(numero):
    resultado = numero * 2  # Variable local: solo existe dentro de duplicar.
    return resultado


doble = duplicar(8)
print(doble)
# print(resultado)  # Descomentar provoca NameError: resultado es local a duplicar.
