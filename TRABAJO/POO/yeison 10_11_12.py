#ejercicio 10
class AlumnoYeison:
    def __init__(self, nombre, nota):
        self.nombre = nombre
        self.nota = nota

    def cambiar_nota(self, nueva):
        self.nota = nueva

    def mostrar(self):
        print(f"{self.nombre} tiene nota {self.nota}")

david = AlumnoYeison("Yeison", 4.0)
david.cambiar_nota(4.8)
david.mostrar()



#ejercicio 11
class AnimalMoreno:
    def hablar(self):
        print("Soy un animal")

class PerroDavid(AnimalMoreno):
    def hablar(self):
        print("Guau!")

nieto = PerroDavid()
nieto.hablar()



#ejercicio 12
class AYeison:
    def metodo_a(self):
        print("Método A")

class BDavid:
    def metodo_b(self):
        print("Método B")

class CHijoMoreno(AYeison, BDavid):
    pass

nieto = CHijoMoreno()
nieto.metodo_a()
nieto.metodo_b()
