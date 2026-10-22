class Estudiante:
    def __init__(self, nombre, ficha, promedio):
        self.nombre = nombre
        self.ficha = ficha
        self.promedio = promedio

    def mostrar_perfil(self):
        print(f"{self.nombre} | Ficha: {self.ficha} | Promedio: {self.promedio:.1f}")

    def aprobo(self):
        return self.promedio >= 3.0


if __name__ == "__main__":
    estudiante_1 = Estudiante("Camila", "F001", 2.8)
    estudiante_2 = Estudiante("Mateo", "F002", 4.1)
    for estudiante in (estudiante_1, estudiante_2):
        estudiante.mostrar_perfil()
        print("Aprobó:", estudiante.aprobo())
