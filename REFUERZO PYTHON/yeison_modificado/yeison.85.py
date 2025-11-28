
class Persona:
    def __init__(self, nombre):
        self._nombre = nombre
    @property
    def nombre(self):
        return self._nombre

yeison_david_moreno = Persona("yeison david moreno")
print(yeison_david_moreno.nombre)



class Calculadora:
    @staticmethod
    def sumar(a, b):
        return a + b

resultado = Calculadora.sumar(10, 15)
print(resultado)