class Direccion:
    def __init__(self, ciudad):
        self.ciudad = ciudad

class Persona:
    def __init__(self, nombre, direccion):
        self.nombre = nombre
        self.direccion = direccion

direccion_kslc = Direccion("Bogotá")
yeison_david_moreno_nieto = Persona("Yeison David Moreno Nieto", direccion_kslc)
print(yeison_david_moreno_nieto.direccion.ciudad)