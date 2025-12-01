class Cuenta:
    def __init__(self, titular, saldo):
        self.titular = titular
        self.saldo = saldo
    def depositar(self, cantidad):
        self.saldo += cantidad

yeison_david_moreno_nieto = Cuenta("Yeison David Moreno Nieto", 1000)
yeison_david_moreno_nieto.depositar(500)
print(yeison_david_moreno_nieto.saldo)