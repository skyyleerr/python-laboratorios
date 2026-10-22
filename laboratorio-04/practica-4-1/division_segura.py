try:
    dividendo = float(input("Dividendo: "))
    divisor = float(input("Divisor: "))
except ValueError:
    print("Entrada que no puede convertirse a número.")
else:
    if divisor == 0:
        print("No se puede dividir entre cero.")
    else:
        print("Resultado:", dividendo / divisor)
