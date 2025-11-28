

class Deportista:
    def entrenar(self):
        print("Entrenando")

class Musico:
    def tocar(self):
        print("Tocando instrumento")

class Persona(Deportista, Musico):
    def __init__(self, nombre):
        self.nombre = nombre

yeison_david_moreno = Persona("yeison david moreno")
yeison_david_moreno.entrenar()
yeison_david_moreno.tocar()



class Persona:
    def __init__(self, nombre):
        self.nombre = nombre
        self.hobbies = []
    def agregar_hobby(self, hobby):
        self.hobbies.append(hobby)

yeison_david_moreno = Persona("yeison david moreno")
yeison_david_moreno.agregar_hobby("Fútbol")
print(yeison_david_moreno.hobbies)