
class Jugador:
    def __init__(self, nombre):
        self.nombre = nombre

class Equipo:
    def __init__(self):
        self.jugadores = []

    def agregar_jugador(self, jugador):
        self.jugadores.append(jugador)

yeison_david_moreno = Jugador("yeison david moreno")
mi_equipo = Equipo()
mi_equipo.agregar_jugador(yeison_david_moreno)
for j in mi_equipo.jugadores:
    print(j.nombre)




class Vehiculo:
    def __init__(self, tipo, velocidad):
        self.tipo = tipo
        self.velocidad = velocidad
    def acelerar(self, aumento):
        self.velocidad += aumento

yeison_david_moreno = Vehiculo("Coche", 50)
yeison_david_moreno.acelerar(20)
print(yeison_david_moreno.velocidad)
