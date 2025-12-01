
class Estudiante:
    def __init__(self, nombre):
        self.nombre = nombre

class Curso:
    def __init__(self):
        self.estudiantes = []
    def agregar_estudiante(self, estudiante):
        self.estudiantes.append(estudiante)

yeison_david_moreno_nieto = Estudiante("Yeison David Moreno Nieto")
curso = Curso()
curso.agregar_estudiante(yeison_david_moreno_nieto)
print([e.nombre for e in curso.estudiantes])



class Persona:
    def actividad(self):
        print("Realizando actividad")

class Estudiante(Persona):
    def actividad(self):
        print("Estudiando")

yeison_david_moreno_nieto = Estudiante()
yeison_david_moreno_nieto.actividad()
class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad
    def cumplir_anos(self):
        self.edad += 1

yeison_david_moreno_nieto = Persona("Yeison David Moreno Nieto", 25)
yeison_david_moreno_nieto.cumplir_anos()
print(yeison_david_moreno_nieto.edad)



