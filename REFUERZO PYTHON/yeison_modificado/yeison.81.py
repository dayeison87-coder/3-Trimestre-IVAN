

class Producto:
    def __init__(self, nombre, precio):
        self.nombre = nombre
        self.precio = precio
    def __str__(self):
        return f"{self.nombre} cuesta {self.precio} USD"

yeison_david_moreno = Producto("Mouse", 25)
print(yeison_david_moreno)



class Vehiculo:
    def __init__(self, tipo, velocidad):
        self.tipo = tipo
        self.velocidad = velocidad
    def __repr__(self):
        return f"Vehiculo('{self.tipo}', {self.velocidad})"

yeison_david_moreno = Vehiculo("Bicicleta", 20)
print(repr(yeison_david_moreno))