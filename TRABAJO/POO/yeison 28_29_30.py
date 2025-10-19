#ejercicio 28
class ContadorNieto:
    def __init__(self):
        self.contador = 0

    def incrementar(self):
        self.contador += 1
        print("Contador:", self.contador)

david = ContadorNieto()
for i in range(3):
    david.incrementar()



#ejercicio 29
class MultiplicadorYeison:
    def multiplicar(self, a, b):
        return a * b

moreno = MultiplicadorYeison()
print(moreno.multiplicar(6, 7))



#ejercicio 30
class EstudianteDavid:
    def __init__(self, nombre):
        self.nombre = nombre

class CursoYeison:
    def __init__(self):
        self.estudiantes = []

    def agregar_estudiante(self, estudiante):
        self.estudiantes.append(estudiante)

curso_moreno = CursoYeison()
curso_moreno.agregar_estudiante(EstudianteDavid("Nieto"))
print(curso_moreno.estudiantes[0].nombre)
