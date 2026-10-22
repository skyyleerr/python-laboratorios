class Saludo:
    def __init__(self, nombre):
        self.nombre = nombre

    def mostrar(self):
        print(f"Hola, {self.nombre}")


if __name__ == "__main__":
    saludo = Saludo("Ana")
    saludo.mostrar()
