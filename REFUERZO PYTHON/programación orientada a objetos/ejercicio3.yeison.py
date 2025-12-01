
class Persona:
    def __init__(self, nombre):
        self.nombre = nombre

class Empleado(Persona):
    def __init__(self, nombre, salario):
        super().__init__(nombre)
        self.salario = salario

yeison_david_moreno_nieto = Empleado("Yeison David Moreno Nieto", 3000)
print(yeison_david_moreno_nieto.nombre, yeison_david_moreno_nieto.salario)
 

