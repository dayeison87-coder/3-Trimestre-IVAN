
class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

yeison_david_moreno = Persona("yeison david moreno", 25)
print(f"{yeison_david_moreno.nombre} tiene {yeison_david_moreno.edad} años")



class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad
    def cumplir_anos(self):
        self.edad += 1

yeison_david_moreno = Persona("yeison david moreno", 25)
yeison_david_moreno.cumplir_anos()
print(yeison_david_moreno.edad)

