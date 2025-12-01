

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

yeison_david_moreno_nieto = Estudiante("Yeison David Moreno Nieto", 75)
curso = Curso()
curso.agregar(yeison_david_moreno_nieto)
print(curso.aprobados())


