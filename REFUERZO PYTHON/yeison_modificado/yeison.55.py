 

class Secreto:
    def __init__(self, mensaje):
        self.__mensaje = mensaje
    def revelar(self):
        print(self.__mensaje)

yeison_david_moreno = Secreto("yeison david moreno")
yeison_david_moreno.revelar()



class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.set_edad(edad)

    def set_edad(self, edad):
        if edad < 0:
            self.edad = 0
        else:
            self.edad = edad

yeison_david_moreno = Persona("yeison david moreno", -5)
print(yeison_david_moreno.edad)