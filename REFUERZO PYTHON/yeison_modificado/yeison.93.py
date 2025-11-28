
class Vehiculo:
    def __init__(self, tipo, velocidad):
        self.tipo = tipo
        self.velocidad = velocidad
    def __str__(self):
        return f"{self.tipo} a {self.velocidad} km/h"

yeison_david_moreno = Vehiculo("Coche", 100)
print(yeison_david_moreno)




class Libro:
    def __init__(self, titulo):
        self.titulo = titulo

class Biblioteca:
    def __init__(self):
        self.libros = []
    def agregar_libro(self, libro):
        self.libros.append(libro)
    def buscar(self, titulo):
        for l in self.libros:
            if l.titulo == titulo:
                return l
        return None

yeison_david_moreno = Libro("Python Intermedio")
biblioteca = Biblioteca()
biblioteca.agregar_libro(yeison_david_moreno)
print(biblioteca.buscar("Python Intermedio").titulo)