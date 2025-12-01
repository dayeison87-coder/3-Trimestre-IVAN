class Nadador:
    def nadar(self):
        print("Nadando")

class Corredor:
    def correr(self):
        print("Corriendo")

class Atleta(Nadador, Corredor):
    def __init__(self, nombre):
        self.nombre = nombre

yeison_david_moreno_nieto = Atleta("Yeison David Moreno Nieto")
yeison_david_moreno_nieto.nadar()
yeison_david_moreno_nieto.correr()