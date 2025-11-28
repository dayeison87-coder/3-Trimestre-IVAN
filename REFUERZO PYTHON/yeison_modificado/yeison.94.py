
class Estudiante:
    def __init__(self, nombre):
        self.nombre = nombre

class Curso:
    def __init__(self):
        self.estudiantes = []
    def agregar_estudiante(self, estudiante):
        self.estudiantes.append(estudiante)

yeison_david_moreno = Estudiante("yeison david moreno")
curso = Curso()
curso.agregar_estudiante(yeison_david_moreno)
print([e.nombre for e in curso.estudiantes])



class Persona:
    def actividad(self):
        print("Realizando actividad")

class Estudiante(Persona):
    def actividad(self):
        print("Estudiando")

yeison_david_moreno = Estudiante()
yeison_david_moreno.actividad()
class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad
    def cumplir_anos(self):
        self.edad += 1

yeison_david_moreno = Persona("yeison david moreno", 25)
yeison_david_moreno.cumplir_anos()
print(yeison_david_moreno.edad)



class Vehiculo:
    def __init__(self, tipo, velocidad):
        self.tipo = tipo
        self.velocidad = velocidad
    def es_mas_rapido_que(self, otro):
        return self.velocidad > otro.velocidad

v1 = Vehiculo("Moto", 120)
v2 = Vehiculo("Coche", 100)
yeison_david_moreno = v1.es_mas_rapido_que(v2)
print(yeison_david_moreno)