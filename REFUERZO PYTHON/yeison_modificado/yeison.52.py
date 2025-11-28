

class Curso:
    def __init__(self, nombre):
        self.nombre = nombre
        self.estudiantes = []

    def agregar_estudiante(self, estudiante):
        self.estudiantes.append(estudiante)

yeison_david_moreno = Curso("Matemáticas")
yeison_david_moreno.agregar_estudiante("yeison david moreno")
print(yeison_david_moreno.estudiantes)



class Persona:
    def __init__(self, nombre):
        self.nombre = nombre
    def crear_hijo(self):
        return Persona(self.nombre + " Jr.")

yeison_david_moreno = Persona("yeison david moreno")
hijo = yeison_david_moreno.crear_hijo()
print(hijo.nombre)