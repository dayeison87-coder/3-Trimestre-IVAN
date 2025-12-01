

class Persona:
    def __init__(self, nombre):
        self._nombre = nombre
    @property
    def nombre(self):
        return self._nombre
    @nombre.setter
    def nombre(self, nuevo_nombre):
        self._nombre = nuevo_nombre

yeison_david_moreno_nieto = Persona("Yeison David Moreno Nieto")
yeison_david_moreno_nieto.nombre = "Yeison Nieto"
print(yeison_david_moreno_nieto.nombre)

