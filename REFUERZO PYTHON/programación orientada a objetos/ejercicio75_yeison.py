class CuentaBancaria:
    def __init__(self, titular, saldo):
        self.titular = titular
        self.saldo = saldo
    def retirar(self, cantidad):
        if cantidad <= self.saldo:
            self.saldo -= cantidad
        else:
            print("Saldo insuficiente")

yeison_david_moreno_nieto = CuentaBancaria("Yeison David Moreno Nieto", 1000)
yeison_david_moreno_nieto.retirar(200)
print(yeison_david_moreno_nieto.saldo)