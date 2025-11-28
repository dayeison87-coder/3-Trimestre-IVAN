

class Producto:
    def __init__(self, nombre, cantidad):
        self.nombre = nombre
        self.cantidad = cantidad

class Tienda:
    def __init__(self):
        self.inventario = []
    def agregar_producto(self, producto):
        self.inventario.append(producto)

yeison_david_moreno = Producto("Laptop", 5)
mi_tienda = Tienda()
mi_tienda.agregar_producto(yeison_david_moreno)
print([(p.nombre, p.cantidad) for p in mi_tienda.inventario])



class Vehiculo:
    def __init__(self, tipo, velocidad):
        self.tipo = tipo
        self.velocidad = velocidad
    def acelerar(self, incremento):
        self.velocidad += incremento
    def frenar(self, decremento):
        self.velocidad -= decremento

yeison_david_moreno = Vehiculo("Coche", 60)
yeison_david_moreno.acelerar(20)
yeison_david_moreno.frenar(10)
print(yeison_david_moreno.velocidad)