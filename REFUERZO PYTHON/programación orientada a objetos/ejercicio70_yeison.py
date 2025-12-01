class Persona:
    def __init__(self, nombre):
        self.__nombre = nombre
    def mostrar_nombre(self):
        print(self.__nombre)

yeison_david_moreno_nieto = Persona("Yeison David Moreno Nieto")
yeison_david_moreno_nieto.mostrar_nombre()