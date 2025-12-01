class Persona:
    def __init__(self, nombre):
        self.nombre = nombre
        self.amigos = []
    def agregar_amigo(self, amigo):
        self.amigos.append(amigo)

yeison_david_moreno_nieto = Persona("Yeison David Moreno Nieto")
juan = Persona("pepe")
yeison_david_moreno_nieto.agregar_amigo(juan)
print([a.nombre for a in yeison_david_moreno_nieto.amigos])