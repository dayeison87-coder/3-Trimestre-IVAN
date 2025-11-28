

class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad
    def presentarse(self):
        print(f"Hola, soy {self.nombre} y tengo {self.edad} años")

yeison_david_moreno = Persona("yeison david moreno", 25)
yeison_david_moreno.presentarse()



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