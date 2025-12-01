class Persona:
    def __init__(self, nombre):
        self.nombre = nombre
        self.datos = {}

yeison_david_moreno_nieto = Persona("Yeison David Moreno Nieto")
yeison_david_moreno_nieto.datos["edad"] = 25
print(yeison_david_moreno_nieto.datos)