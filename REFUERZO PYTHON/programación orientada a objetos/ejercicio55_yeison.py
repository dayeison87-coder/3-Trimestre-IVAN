
class Empleado:
    def __init__(self, nombre, salario):
        self.nombre = nombre
        self.salario = salario
    def aumentar_salario(self, porcentaje):
        self.salario += self.salario * porcentaje / 100

yeison_david_moreno_nieto = Empleado("Yeison David Moreno Nieto", 3000)
yeison_david_moreno_nieto.aumentar_salario(10)
print(yeison_david_moreno_nieto.salario)