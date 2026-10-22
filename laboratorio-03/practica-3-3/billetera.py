class Billetera:
    def __init__(self, titular, saldo=0):
        if not titular.strip():
            raise ValueError("El titular no puede estar vacío.")
        if saldo < 0:
            raise ValueError("El saldo inicial no puede ser negativo.")
        self._titular = titular.strip()
        self._saldo = saldo

    def registrar_ingreso(self, monto):
        if monto <= 0:
            return False
        self._saldo += monto
        return True

    def registrar_gasto(self, monto):
        if monto <= 0 or monto > self._saldo:
            return False
        self._saldo -= monto
        return True

    def consultar_saldo(self):
        return self._saldo


if __name__ == "__main__":
    billetera_ana = Billetera("Ana")
    billetera_luis = Billetera("Luis")
    billetera_ana.registrar_ingreso(100000)
    billetera_ana.registrar_gasto(25000)
    billetera_ana.registrar_gasto(10000)
    billetera_luis.registrar_ingreso(5000)
    print("Saldo de Ana:", billetera_ana.consultar_saldo())
    print("Saldo de Luis:", billetera_luis.consultar_saldo())
    print("Gasto excesivo rechazado:", not billetera_luis.registrar_gasto(9000))
