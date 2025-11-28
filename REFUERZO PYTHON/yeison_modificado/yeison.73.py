
class Persona:
    def __init__(self, nombre):
        self.nombre = nombre

class Empleado(Persona):
    def __init__(self, nombre, salario):
        super().__init__(nombre)
        self.salario = salario

yeison_david_moreno = Empleado("yeison david moreno", 3000)
print(yeison_david_moreno.nombre, yeison_david_moreno.salario)
 

class Persona:
    def __init__(self, nombre):
        self.nombre = nombre
    def duplicar(self):
        return Persona(self.nombre + " Jr.")

yeison_david_moreno = Persona("yeison david moreno")
nuevo_kevin = yeison_david_moreno.duplicar()
print(nuevo_kevin.nombre)