class Vehiculo:
    def __init__(self, marca, modelo): self.marca, self.modelo = marca, modelo
class Motocicleta(Vehiculo):
    def __init__(self, marca, modelo, cilindraje):
        super().__init__(marca, modelo)
        if cilindraje <= 0: raise ValueError("El cilindraje debe ser positivo.")
        self.cilindraje = cilindraje
for moto in (Motocicleta("Honda", "CB500", 500), Motocicleta("Yamaha", "MT-07", 689)):
    print(moto.marca, moto.modelo, moto.cilindraje, "cc")
