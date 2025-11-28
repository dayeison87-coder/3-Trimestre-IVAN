

class Estudiante:
    def __init__(self, nombre):
        self.nombre = nombre

class Curso:
    def __init__(self):
        self.estudiantes = []

    def agregar_estudiante(self, estudiante):
        self.estudiantes.append(estudiante)

yeison_david_moreno = Estudiante("yeison david moreno")
matematicas = Curso()
matematicas.agregar_estudiante(yeison_david_moreno)
print([e.nombre for e in matematicas.estudiantes])

class Persona:
    pass

yeison_david_moreno = Persona()
yeison_david_moreno.nombre = "yeison david moreno"
print(yeison_david_moreno.nombre)