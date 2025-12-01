

class Empleado:
    def __init__(self, nombre, salario):
        self.nombre = nombre
        self.salario = salario
    def calcular_bono(self):
        return self.salario * 0.1

yeison_david_moreno_nieto = Empleado("Yeison David Moreno Nieto", 3000)
print(yeison_david_moreno_nieto.calcular_bono())



