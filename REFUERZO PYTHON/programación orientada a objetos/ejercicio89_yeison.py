class Empleado:
    def __init__(self, nombre, salario):
        self.nombre = nombre
        self.salario = salario

class Gerente(Empleado):
    def __init__(self, nombre, salario, departamento):
        super().__init__(nombre, salario)
        self.departamento = departamento

yeison_david_moreno_nieto = Gerente("Yeison David Moreno Nieto", 5000, "Ventas")
print(yeison_david_moreno_nieto.nombre, yeison_david_moreno_nieto.departamento)