

class Persona:
    def __init__(self, nombre):
        self.nombre = nombre

class Estudiante(Persona):
    def __init__(self, nombre, carrera):
        super().__init__(nombre)
        self.carrera = carrera

yeison_david_moreno_nieto = Estudiante("Yeison David Moreno Nieto", "Ingeniería")
print(yeison_david_moreno_nieto.nombre, yeison_david_moreno_nieto.carrera)


