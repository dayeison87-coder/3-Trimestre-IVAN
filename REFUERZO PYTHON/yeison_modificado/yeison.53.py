 

class Banco:
    def __init__(self, titular, saldo):
        self.titular = titular
        self.__saldo = saldo
    def mostrar_saldo(self):
        print(self.__saldo)

yeison_david_moreno = Banco("yeison david moreno", 1000)
yeison_david_moreno.mostrar_saldo()




class Empleado:
    def __init__(self, nombre, salario):
        self.nombre = nombre
        self.salario = salario

class Gerente(Empleado):
    def __init__(self, nombre, salario, departamento):
        super().__init__(nombre, salario)
        self.departamento = departamento

yeison_david_moreno = Gerente("yeison david moreno", 5000, "Ventas")
print(yeison_david_moreno.nombre, yeison_david_moreno.departamento)