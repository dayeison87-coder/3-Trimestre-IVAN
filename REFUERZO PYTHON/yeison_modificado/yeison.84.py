

class Persona:
    contador = 0
    def __init__(self, nombre):
        self.nombre = nombre
        Persona.contador += 1

yeison_david_moreno1 = Persona("yeison david moreno")
yeison_david_moreno2 = Persona("yeison david moreno")
print(Persona.contador)


class Persona:
    def __init__(self, nombre):
        self.nombre = nombre

personas = []
personas.append(Persona("yeison david moreno"))
personas.append(Persona("Juan"))
for p in personas:
    print(p.nombre)