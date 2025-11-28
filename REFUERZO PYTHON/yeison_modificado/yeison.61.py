
class Producto:
    def __init__(self, nombre, precio):
        self.nombre = nombre
        self.precio = precio

class Tienda:
    def __init__(self):
        self.productos = []

    def agregar_producto(self, producto):
        self.productos.append(producto)

yeison_david_moreno = Producto("Laptop", 1500)
mi_tienda = Tienda()
mi_tienda.agregar_producto(yeison_david_moreno)
for p in mi_tienda.productos:
    print(p.nombre, p.precio)



class Cuenta:
    def __init__(self, titular, saldo):
        self.titular = titular
        self.saldo = saldo
    def depositar(self, cantidad):
        self.saldo += cantidad

yeison_david_moreno = Cuenta("yeison david moreno", 1000)
yeison_david_moreno.depositar(500)
print(yeison_david_moreno.saldo)