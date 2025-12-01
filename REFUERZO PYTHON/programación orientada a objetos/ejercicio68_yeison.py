class Cuenta:
    def __init__(self, titular, saldo):
        self.titular = titular
        self.saldo = saldo
    def interes(self, porcentaje):
        self.saldo += self.saldo * porcentaje / 100

yeison_david_moreno_nieto = Cuenta("Yeison David Moreno Nieto", 1000)
yeison_david_moreno_nieto.interes(5)
print(yeison_david_moreno_nieto.saldo)