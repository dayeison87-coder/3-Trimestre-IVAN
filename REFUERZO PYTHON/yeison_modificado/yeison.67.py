
class Producto:
    def __init__(self, nombre, precio):
        self.nombre = nombre
        self.precio = precio
    def aplicar_descuento(self, porcentaje):
        self.precio *= (1 - porcentaje/100)

yeison_david_moreno = Producto("Camisa", 50)
yeison_david_moreno.aplicar_descuento(20)
print(yeison_david_moreno.precio)


class CuentaBancaria:
    def __init__(self, titular, saldo):
        self.titular = titular
        self.saldo = saldo
    def retirar(self, cantidad):
        if cantidad <= self.saldo:
            self.saldo -= cantidad
        else:
            print("Saldo insuficiente")

yeison_david_moreno = CuentaBancaria("yeison david moreno", 1000)
yeison_david_moreno.retirar(200)
print(yeison_david_moreno.saldo)

