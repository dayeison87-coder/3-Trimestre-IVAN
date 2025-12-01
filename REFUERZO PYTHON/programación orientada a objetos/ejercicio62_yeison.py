
class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad
    def es_mayor(self):
        return self.edad >= 18

yeison_david_moreno_nieto = Persona("Yeison David Moreno Nieto", 25)
print(yeison_david_moreno_nieto.es_mayor())