

class Persona:
    def __init__(self, nombre):
        self._nombre = nombre
    @property
    def nombre(self):
        return self._nombre
    @nombre.setter
    def nombre(self, nuevo_nombre):
        self._nombre = nuevo_nombre

yeison_david_moreno = Persona("yeison david moreno")
yeison_david_moreno.nombre = "yeison moreno"
print(yeison_david_moreno.nombre)


class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad
    def es_mayor(self):
        return self.edad >= 18

yeison_david_moreno = Persona("yeison david moreno", 25)
print(yeison_david_moreno.es_mayor())