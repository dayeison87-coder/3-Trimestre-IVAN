

class Nadador:
    def nadar(self):
        print("Nadando")

class Corredor:
    def correr(self):
        print("Corriendo")

class Atleta(Nadador, Corredor):
    pass

yeison_david_moreno = Atleta()
yeison_david_moreno.nadar()
yeison_david_moreno.correr()


class Persona:
    def __init__(self, nombre):
        self.nombre = nombre
        self.datos = {}

yeison_david_moreno = Persona("yeison david moreno")
yeison_david_moreno.datos["edad"] = 25
print(yeison_david_moreno.datos)