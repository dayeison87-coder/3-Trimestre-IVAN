

class Punto:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def sumar(self, otro):
        return Punto(self.x + otro.x, self.y + otro.y)

p1 = Punto(2, 3)
p2 = Punto(4, 5)
yeison_david_moreno = p1.sumar(p2)
print(yeison_david_moreno.x, yeison_david_moreno.y)



class Producto:
    def __init__(self, nombre, precio):
        self.nombre = nombre
        self.precio = precio

class Pedido:
    def __init__(self):
        self.productos = []
    def agregar(self, producto):
        self.productos.append(producto)
    def total(self):
        return sum(p.precio for p in self.productos)

yeison_david_moreno = Producto("Teclado", 30)
pedido1 = Pedido()
pedido1.agregar(yeison_david_moreno)
print(pedido1.total())