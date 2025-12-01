class Profesor:
    def __init__(self, nombre):
        self.nombre = nombre
        self.materias = []

    def agregar_materia(self, materia):
        self.materias.append(materia)

yeison_david_moreno_nieto = Profesor("Yeison David Moreno Nieto")
yeison_david_moreno_nieto.agregar_materia("Matemáticas")
print(yeison_david_moreno_nieto.materias)