import unidades


def leer_numero(mensaje):
    while True:
        try:
            return float(input(mensaje))
        except ValueError:
            print("Debes escribir un número válido.")


if __name__ == "__main__":
    kilometros = leer_numero("Kilómetros: ")
    celsius = leer_numero("Temperatura en Celsius: ")
    print(f"{kilometros:g} km = {unidades.kilometros_a_metros(kilometros):g} m")
    print(f"{celsius:g} °C = {unidades.celsius_a_fahrenheit(celsius):g} °F")
