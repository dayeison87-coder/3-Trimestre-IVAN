
class Producto:
    def __init__(self, nombre, stock):
        self.nombre = nombre
        self.stock = stock
    def vender(self, cantidad):
        if cantidad <= self.stock:
            self.stock -= cantidad
        else:
            print("Stock insuficiente")

yeison_david_moreno_nieto = Producto("Mouse", 10)
yeison_david_moreno_nieto.vender(3)
print(yeison_david_moreno_nieto.stock)




