
class Producto:
    def __init__(self, nombre, stock):
        self.nombre = nombre
        self.stock = stock
    def vender(self, cantidad):
        if cantidad <= self.stock:
            self.stock -= cantidad
        else:
            print("Stock insuficiente")

yeison_david_moreno = Producto("Mouse", 10)
yeison_david_moreno.vender(3)
print(yeison_david_moreno.stock)




class Empleado:
    def __init__(self, nombre, cargo):
        self.nombre = nombre
        self.cargo = cargo
    def info(self):
        print(f"{self.nombre} trabaja como {self.cargo}")

yeison_david_moreno = Empleado("yeison david moreno", "Ingeniero")
yeison_david_moreno.info()
def cuadrados_mayores_que(yeison_david_moreno_lista, yeison_david_moreno_n):
    return [x**2 for x in yeison_david_moreno_lista if x**2 > yeison_david_moreno_n]

print(cuadrados_mayores_que([1,2,3,4,5], 10))



def numeros_pares(yeison_david_moreno_inicio, yeison_david_moreno_fin):
    return [x for x in range(yeison_david_moreno_inicio, yeison_david_moreno_fin+1) if x%2==0]

print(numeros_pares(1,10))