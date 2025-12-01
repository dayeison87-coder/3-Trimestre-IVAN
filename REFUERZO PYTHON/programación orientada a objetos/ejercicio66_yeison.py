class Nadador:
    def nadar(self):
        print("Nadando")

class Corredor:
    def correr(self):
        print("Corriendo")

class Atleta(Nadador, Corredor):
    pass

yeison_david_moreno_nieto = Atleta()
yeison_david_moreno_nieto.nadar()
yeison_david_moreno_nieto.correr()