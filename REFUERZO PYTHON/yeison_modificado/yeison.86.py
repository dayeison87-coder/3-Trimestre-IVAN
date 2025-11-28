
class Vehiculo:
    def __init__(self, tipo, velocidad):
        self.tipo = tipo
        self.velocidad = velocidad
    def obtener_velocidad(self):
        return self.velocidad

yeison_david_moreno = Vehiculo("Moto", 80)
print(yeison_david_moreno.obtener_velocidad())



class Empleado:
    def __init__(self, nombre, salario):
        self.nombre = nombre
        self.salario = salario
    def aumentar_salario(self, porcentaje):
        self.salario += self.salario * porcentaje / 100

yeison_david_moreno = Empleado("yeison david moreno", 3000)
yeison_david_moreno.aumentar_salario(10)
print(yeison_david_moreno.salario)