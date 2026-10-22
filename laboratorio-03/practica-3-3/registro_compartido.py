class RegistroIncorrecto:
    elementos = []  # Error didáctico: atributo mutable compartido por todas las instancias.


primero_mal = RegistroIncorrecto()
segundo_mal = RegistroIncorrecto()
primero_mal.elementos.append("Teclado")
print("Demostración de lista compartida:", segundo_mal.elementos)


class Registro:
    def __init__(self):
        self.elementos = []  # Cada objeto obtiene su propia lista.


primero = Registro()
segundo = Registro()
primero.elementos.append("Teclado")
print("Primero:", primero.elementos)
print("Segundo:", segundo.elementos)
