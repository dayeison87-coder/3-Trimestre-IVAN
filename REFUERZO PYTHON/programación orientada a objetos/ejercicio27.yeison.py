

class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad
    def presentarse(self):
        print(f"Hola, soy {self.nombre} y tengo {self.edad} años")

yeison_david_moreno_nieto = Persona("Yeison David Moreno Nieto", 25)
yeison_david_moreno_nieto.presentarse()



