#EJERCICIO 4
class CuadradoYeison:
    def __init__(self, lado):
        self.lado = lado

    def area(self):
        return self.lado ** 2

david = CuadradoYeison(4)
print("Área:", david.area())



#EJERCICIO 5
class RectanguloMoreno:
    def __init__(self, base, altura):
        self.base = base
        self.altura = altura

    def perimetro(self):
        return 2 * (self.base + self.altura)

nieto = RectanguloMoreno(5, 3)
print("Perímetro:", nieto.perimetro())



#EJERCICIO 6
class CalculadoraYeison:
    def sumar(self, a, b):
        return a + b

calc_david = CalculadoraYeison()
print(calc_david.sumar(5, 7))
