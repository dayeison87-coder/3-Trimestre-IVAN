

class Persona:
    def __init__(self, nombre):
        self.nombre = nombre

yeison_david_moreno = Persona("yeison david moreno")
print(yeison_david_moreno.nombre)



class Persona:
    def __init__(self, nombre):
        self.nombre = nombre
    def saludar(self):
        print(f"Hola, soy {self.nombre}")

yeison_david_moreno = Persona("yeison david moreno")
yeison_david_moreno.saludar()



