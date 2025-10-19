#ejercicio 46
class ContadorLetrasMoreno:
    def contar(self, texto):
        return len(texto.replace(" ", ""))

nieto = ContadorLetrasMoreno()
print(nieto.contar("David Yeison"))



#ejercicio 47
class TrianguloYeison:
    def __init__(self, base, altura):
        self.base = base
        self.altura = altura

    def area(self):
        return (self.base * self.altura) / 2

david = TrianguloYeison(6, 3)
print("Área:", david.area())



#ejercicio 48
class NombresMoreno:
    def __init__(self):
        self.nombres = set()

    def agregar(self, nombre):
        self.nombres.add(nombre)

    def mostrar(self):
        print(self.nombres)

yeison = NombresMoreno()
yeison.agregar("David")
yeison.agregar("David")
yeison.agregar("Nieto")
yeison.mostrar()
