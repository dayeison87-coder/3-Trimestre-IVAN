class Luz:
    def __init__(self):
        self.encendida = False
    def cambiar_estado(self):
        self.encendida = not self.encendida

yeison_david_moreno_nieto = Luz()
yeison_david_moreno_nieto.cambiar_estado()
print(yeison_david_moreno_nieto.encendida)