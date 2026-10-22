class Persona:
    def __init__(self, nombre):
        self.nombre = nombre

    def mostrar(self):
        print(self.nombre)  # Corregido: el atributo se llama nombre, no nombree.


if __name__ == "__main__":
    Persona("Ana").mostrar()
