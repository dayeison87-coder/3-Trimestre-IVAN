

class Vehiculo:
    def __init__(self, tipo, capacidad):
        self.tipo = tipo
        self.capacidad = capacidad

yeison_david_moreno = Vehiculo("Camión", 1000)
print(yeison_david_moreno.tipo, yeison_david_moreno.capacidad)



class Nadador:
    def nadar(self):
        print("Nadando")

class Corredor:
    def correr(self):
        print("Corriendo")

class Atleta(Nadador, Corredor):
    def __init__(self, nombre):
        self.nombre = nombre

yeison_david_moreno = Atleta("yeison david moreno")
yeison_david_moreno.nadar()
yeison_david_moreno.correr()