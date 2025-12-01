

class Estudiante:
    def __init__(self, nombre, notas):
        self.nombre = nombre
        self.notas = notas
    def promedio(self):
        return sum(self.notas) / len(self.notas)

yeison_david_moreno_nieto = Estudiante("Yeison David Moreno Nieto", [80, 90, 70])
print(yeison_david_moreno_nieto.promedio())


