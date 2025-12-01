
class Persona:
    def __init__(self, nombre):
        self.nombre = nombre
    def saludar(self):
        print(f"Hola, soy {self.nombre}")

yeison_david_moreno_nieto = Persona("Yeison David Moreno Nieto")
yeison_david_moreno_nieto.saludar()
