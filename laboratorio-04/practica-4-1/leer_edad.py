try:
    edad = int(input("Edad: "))
except ValueError:
    print("Error de conversión: escribe la edad como número entero.")
else:
    if edad < 0 or edad > 120:
        print("Edad fuera del rango permitido (0 a 120).")
    else:
        print("Edad aceptada:", edad)
