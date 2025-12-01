class Contraseña:
    def __init__(self, clave):
        self.__clave = clave
    def mostrar_clave(self):
        print(self.__clave)

yeison_david_moreno_nieto = Contraseña("12345")
yeison_david_moreno_nieto.mostrar_clave()