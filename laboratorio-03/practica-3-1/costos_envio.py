def calcular_cobro(valor_compra, envio=10000):
    return valor_compra + envio


if __name__ == "__main__":
    print("Con envío predeterminado:", calcular_cobro(50000))
    print("Con envío gratuito:", calcular_cobro(50000, envio=0))
