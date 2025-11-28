

class Persona:
    def __init__(self, nombre):
        self.nombre = nombre

class Estudiante(Persona):
    def estudiar(self):
        print(f"{self.nombre} está estudiando")

yeison_david_moreno = Estudiante("yeison david moreno")
yeison_david_moreno.estudiar()


class Persona:
    def __init__(self, nombre):
        self.__nombre = nombre
    def mostrar_nombre(self):
        print(self.__nombre)

yeison_david_moreno = Persona("yeison david moreno")
yeison_david_moreno.mostrar_nombre()