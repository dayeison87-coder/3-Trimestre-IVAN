
class Persona:
    def __init__(self, nombre):
        self._nombre = nombre
    @property
    def nombre(self):
        return self._nombre

yeison_david_moreno_nieto = Persona("Yeison David Moreno Nieto")
print(yeison_david_moreno_nieto.nombre)



