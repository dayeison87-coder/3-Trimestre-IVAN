class Persona:
    def __init__(self, nombre):
        self.nombre = nombre
    def __repr__(self):
        return f"Persona('{self.nombre}')"

yeison_david_moreno_nieto = Persona("Yeison David Moreno Nieto")
print(repr(yeison_david_moreno_nieto))