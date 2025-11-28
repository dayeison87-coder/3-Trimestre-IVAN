
 

class Persona:
    especie = "Humano"
    def __init__(self, nombre):
        self.nombre = nombre

yeison_david_moreno = Persona("yeison david moreno")
print(yeison_david_moreno.nombre, "-", Persona.especie)




class Luz:
    def __init__(self):
        self.encendida = False
    def cambiar_estado(self):
        self.encendida = not self.encendida

yeison_david_moreno = Luz()
yeison_david_moreno.cambiar_estado()
print(yeison_david_moreno.encendida)
