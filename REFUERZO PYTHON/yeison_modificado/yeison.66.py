from abc import ABC, abstractmethod

class Animal(ABC):
    @abstractmethod
    def sonido(self):
        pass

class Perro(Animal):
    def sonido(self):
        print("Guau")

yeison_david_moreno = Perro()
yeison_david_moreno.sonido()


class Jugador:
    def __init__(self, nombre):
        self.nombre = nombre

class Juego:
    def __init__(self):
        self.jugadores = []

    def agregar_jugador(self, jugador):
        self.jugadores.append(jugador)

yeison_david_moreno = Jugador("yeison david moreno")
juego1 = Juego()
juego1.agregar_jugador(yeison_david_moreno)
for j in juego1.jugadores:
    print(j.nombre)