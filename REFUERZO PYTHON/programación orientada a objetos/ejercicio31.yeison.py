

class Auto:
    def __init__(self, marca):
        self.marca = marca
        self.encendido = False
    def encender(self):
        self.encendido = True
    def apagar(self):
        self.encendido = False

yeison_david_moreno_nieto = Auto("Toyota")
yeison_david_moreno_nieto.encender()
print(yeison_david_moreno_nieto.encendido)




