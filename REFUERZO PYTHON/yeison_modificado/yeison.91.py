
class Cuenta:
    def __init__(self, titular, saldo):
        self.titular = titular
        self.saldo = saldo
    def transferir(self, otra_cuenta, cantidad):
        if cantidad <= self.saldo:
            self.saldo -= cantidad
            otra_cuenta.saldo += cantidad

cuenta1 = Cuenta("yeison david moreno", 1000)
cuenta2 = Cuenta("Juan", 500)
cuenta1.transferir(cuenta2, 300)
print(cuenta1.saldo, cuenta2.saldo)


class Alumno:
    def __init__(self, nombre):
        self.nombre = nombre
        self.asistencias = 0
    def registrar_asistencia(self):
        self.asistencias += 1

yeison_david_moreno = Alumno("yeison david moreno")
yeison_david_moreno.registrar_asistencia()
print(yeison_david_moreno.asistencias)