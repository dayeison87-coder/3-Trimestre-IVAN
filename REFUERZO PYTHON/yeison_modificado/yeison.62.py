

class Persona:
    def __init__(self, nombre):
        self.nombre = nombre
    def __str__(self):
        return f"Persona: {self.nombre}"

yeison_david_moreno = Persona("yeison david moreno")
print(yeison_david_moreno)



class Persona:
    def __init__(self, nombre):
        self.nombre = nombre
    def __repr__(self):
        return f"Persona('{self.nombre}')"

yeison_david_moreno = Persona("yeison david moreno")
print(repr(yeison_david_moreno))