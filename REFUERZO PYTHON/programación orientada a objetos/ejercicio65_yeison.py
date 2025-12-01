class Persona:
    def __init__(self, nombre):
        self.nombre = nombre
    def saludar(self, otra_persona):
        print(f"Hola {otra_persona}, soy {self.nombre}")

yeison_david_moreno_nieto = Persona("Yeison David Moreno Nieto")
yeison_david_moreno_nieto.saludar("Juan")