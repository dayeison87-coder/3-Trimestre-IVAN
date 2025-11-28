

class Auto:
    def __init__(self, marca):
        self.marca = marca
        self.encendido = False
    def encender(self):
        self.encendido = True
    def apagar(self):
        self.encendido = False

yeison_david_moreno = Auto("Toyota")
yeison_david_moreno.encender()
print(yeison_david_moreno.encendido)




class Equipo:
    def __init__(self, nombre):
        self.nombre = nombre
        self.puntos = 0
    def ganar_partido(self):
        self.puntos += 3

yeison_david_moreno = Equipo("yeison david moreno FC")
yeison_david_moreno.ganar_partido()
print(yeison_david_moreno.puntos)