

class Persona:
    contador = 0
    def __init__(self, nombre):
        self.nombre = nombre
        Persona.contador += 1

yeison_david_moreno_nieto1 = Persona("Yeison David Moreno Nieto")
yeison_david_moreno_nieto2 = Persona("Yeison David Moreno Nieto")
print(Persona.contador)


