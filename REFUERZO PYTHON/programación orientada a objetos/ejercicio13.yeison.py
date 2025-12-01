 

class Secreto:
    def __init__(self, mensaje):
        self.__mensaje = mensaje
    def revelar(self):
        print(self.__mensaje)

yeison_david_moreno_nieto = Secreto("Yeison David Moreno Nieto")
yeison_david_moreno_nieto.revelar()

