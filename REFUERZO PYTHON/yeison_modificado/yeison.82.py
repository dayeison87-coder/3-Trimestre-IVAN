
class Persona:
    contador = 0
    def __init__(self, nombre):
        self.nombre = nombre
        Persona.contador += 1

yeison_david_moreno1 = Persona("yeison david moreno")
yeison_david_moreno2 = Persona("Juan")
print(Persona.contador)



class Persona:
    def __init__(self, nombre):
        self.nombre = nombre
    def crear_amigo(self, nombre_amigo):
        return Persona(nombre_amigo)

yeison_david_moreno = Persona("yeison david moreno")
amigo = yeison_david_moreno.crear_amigo("Juan")
print(amigo.nombre)