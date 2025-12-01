class Poligono:
    def __init__(self, lados):
        self.lados = lados

class Cuadrado(Poligono):
    def __init__(self, lado):
        super().__init__(4)
        self.lado = lado
    def area(self):
        return self.lado ** 2

yeison_david_moreno_nieto = Cuadrado(5)
print(yeison_david_moreno_nieto.area())




