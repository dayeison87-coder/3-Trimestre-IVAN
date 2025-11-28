
class Vehiculo:
    def __init__(self, tipo, velocidad):
        self.tipo = tipo
        self.velocidad = velocidad
    def __gt__(self, otro):
        return self.velocidad > otro.velocidad

v1 = Vehiculo("Coche", 120)
v2 = Vehiculo("Moto", 100)
yeison_david_moreno = v1 > v2
print(yeison_david_moreno)


class Persona:
    def __init__(self, nombre):
        self.nombre = nombre
        self.amigos = []
    def agregar_amigo(self, amigo):
        self.amigos.append(amigo)

yeison_david_moreno = Persona("yeison david moreno")
juan = Persona("Juan")
yeison_david_moreno.agregar_amigo(juan)
print([a.nombre for a in yeison_david_moreno.amigos])