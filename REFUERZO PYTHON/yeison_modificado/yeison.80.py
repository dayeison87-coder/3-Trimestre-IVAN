

class Estudiante:
    def __init__(self, nombre, nota):
        self.nombre = nombre
        self.nota = nota

class Curso:
    def __init__(self):
        self.estudiantes = []
    def agregar(self, estudiante):
        self.estudiantes.append(estudiante)
    def aprobados(self):
        return [e.nombre for e in self.estudiantes if e.nota >= 60]

yeison_david_moreno = Estudiante("yeison david moreno", 75)
curso = Curso()
curso.agregar(yeison_david_moreno)
print(curso.aprobados())


class Persona:
    def __init__(self, nombre):
        self.nombre = nombre
    def saludar(self, otra_persona):
        print(f"Hola {otra_persona}, soy {self.nombre}")

yeison_david_moreno = Persona("yeison david moreno")
yeison_david_moreno.saludar("Juan")