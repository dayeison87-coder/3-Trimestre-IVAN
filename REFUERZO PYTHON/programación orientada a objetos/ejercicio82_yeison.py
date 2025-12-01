class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad
    def cumplir_anos(self):
        self.edad += 1

yeison_david_moreno_nieto = Persona("Yeison David Moreno Nieto", 25)
yeison_david_moreno_nieto.cumplir_anos()
print(yeison_david_moreno_nieto.edad)