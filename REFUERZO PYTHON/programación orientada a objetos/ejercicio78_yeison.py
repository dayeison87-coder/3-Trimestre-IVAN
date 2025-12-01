class Persona:
    def __init__(self, nombre):
        self.nombre = nombre
        self.atributos = {}

yeison_david_moreno_nieto = Persona("Yeison David Moreno Nieto")
yeison_david_moreno_nieto.atributos["altura"] = 1.75
print(yeison_david_moreno_nieto.atributos)