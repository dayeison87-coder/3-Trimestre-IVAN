
class Persona:
    contador = 0
    def __init__(self, nombre):
        self.nombre = nombre
        Persona.contador += 1
    @classmethod
    def total_personas(cls):
        return cls.contador

yeison_david_moreno_nieto = Persona("Yeison David Moreno Nieto")
otra_persona = Persona("Juan")
print(Persona.total_personas())


