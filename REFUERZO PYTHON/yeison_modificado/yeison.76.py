

class Persona:
    def __init__(self, nombre):
        self.nombre = nombre

class Estudiante(Persona):
    def __init__(self, nombre, carrera):
        super().__init__(nombre)
        self.carrera = carrera

yeison_david_moreno = Estudiante("yeison david moreno", "Ingeniería")
print(yeison_david_moreno.nombre, yeison_david_moreno.carrera)


class Cuenta:
    def __init__(self, titular, saldo):
        self.titular = titular
        self.saldo = saldo
    def interes(self, porcentaje):
        self.saldo += self.saldo * porcentaje / 100

yeison_david_moreno = Cuenta("yeison david moreno", 1000)
yeison_david_moreno.interes(5)
print(yeison_david_moreno.saldo)