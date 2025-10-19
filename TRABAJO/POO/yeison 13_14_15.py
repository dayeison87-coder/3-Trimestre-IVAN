#ejercicio 13
class ProductoDavid:
    def __init__(self, nombre, precio):
        self.nombre = nombre
        self.precio = precio

class TiendaYeison:
    def __init__(self):
        self.productos = []

    def agregar(self, producto):
        self.productos.append(producto)

    def mostrar(self):
        for p in self.productos:
            print(p.nombre, "-", p.precio)

moreno = TiendaYeison()
moreno.agregar(ProductoDavid("Casco", 150000))
moreno.agregar(ProductoDavid("Guantes", 80000))
moreno.mostrar()



#ejercicio 14
class ContadorNieto:
    cantidad = 0

    def __init__(self):
        ContadorNieto.cantidad += 1

yeison = ContadorNieto()
david = ContadorNieto()
moreno = ContadorNieto()
print("Total objetos:", ContadorNieto.cantidad)



#ejercicio 15
class UtilidadesMoreno:
    @staticmethod
    def saludar():
        print("Hola desde un método estático, Yeison!")

UtilidadesMoreno.saludar()
