from abc import ABC, abstractmethod

class Poligono(ABC):
    @abstractmethod
    def area(self):
        pass

class Triangulo(Poligono):
    def __init__(self, base, altura):
        self.base = base
        self.altura = altura
    def area(self):
        return self.base * self.altura / 2

yeison_david_moreno_nieto = Triangulo(10, 5)
print(yeison_david_moreno_nieto.area())