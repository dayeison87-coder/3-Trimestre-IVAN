

class Persona:
    def actividad(self):
        print("Actividad genérica")

class Profesor(Persona):
    def actividad(self):
        print("Enseñando")

yeison_david_moreno = Profesor()
yeison_david_moreno.actividad()


class Persona:
    def __init__(self, nombre):
        self.nombre = nombre
        self.atributos = {}

yeison_david_moreno = Persona("yeison david moreno")
yeison_david_moreno.atributos["altura"] = 1.75
print(yeison_david_moreno.atributos)