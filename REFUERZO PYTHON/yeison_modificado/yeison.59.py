

class Persona:
    contador = 0
    def __init__(self, nombre):
        self.nombre = nombre
        Persona.contador += 1

yeison_david_moreno1 = Persona("yeison david moreno")
yeison_david_moreno2 = Persona("Kevin Cuervo")
print(Persona.contador)




class Persona:
    def __init__(self, nombre):
        self.nombre = nombre
    def __len__(self):
        return len(self.nombre)

yeison_david_moreno = Persona("yeison david moreno")
print(len(yeison_david_moreno))