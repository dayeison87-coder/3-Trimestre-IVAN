

class Persona:
    def __init__(self, nombre):
        self.nombre = nombre
    def __str__(self):
        return f"Persona: {self.nombre}"

yeison_david_moreno_nieto = Persona("Yeison David Moreno Nieto")
print(yeison_david_moreno_nieto)



