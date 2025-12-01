 

class Banco:
    def __init__(self, titular, saldo):
        self.titular = titular
        self.__saldo = saldo
    def mostrar_saldo(self):
        print(self.__saldo)

yeison_david_moreno_nieto = Banco("Yeison David Moreno Nieto", 1000)
yeison_david_moreno_nieto.mostrar_saldo()




