

class Empleado:
    def __init__(self, nombre, salario):
        self.nombre = nombre
        self.salario = salario
    def calcular_bono(self):
        return self.salario * 0.1

yeison_david_moreno = Empleado("yeison david moreno", 3000)
print(yeison_david_moreno.calcular_bono())



class Persona:
    def __init__(self, nombre):
        self.nombre = nombre

class Alumno(Persona):
    def estudiar(self):
        print(f"{self.nombre} está estudiando")

yeison_david_moreno = Alumno("yeison david moreno")
yeison_david_moreno.estudiar()