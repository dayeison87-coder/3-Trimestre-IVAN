

class Curso:
    def __init__(self, nombre):
        self.nombre = nombre
        self.estudiantes = []

    def agregar_estudiante(self, estudiante):
        self.estudiantes.append(estudiante)

yeison_david_moreno_nieto = Curso("software")
yeison_david_moreno_nieto.agregar_estudiante("Yeison David Moreno Nieto")
print(yeison_david_moreno_nieto.estudiantes)



