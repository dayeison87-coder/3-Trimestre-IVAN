

class Deportista:
    def entrenar(self):
        print("Entrenando")

class Musico:
    def tocar(self):
        print("Tocando música")

class Persona(Deportista, Musico):
    def __init__(self, nombre):
        self.nombre = nombre

yeison_david_moreno_nieto = Persona("Yeison David Moreno Nieto")
yeison_david_moreno_nieto.entrenar()
yeison_david_moreno_nieto.tocar()



class Persona:
    def __init__(self, nombre):
        self.nombre = nombre
        self.hobbies = []
    def agregar_hobby(self, hobby):
        self.hobbies.append(hobby)

yeison_david_moreno_nieto = Persona("Yeison David Moreno Nieto")
yeison_david_moreno_nieto.agregar_hobby("voleibol")
print(yeison_david_moreno_nieto.hobbies)