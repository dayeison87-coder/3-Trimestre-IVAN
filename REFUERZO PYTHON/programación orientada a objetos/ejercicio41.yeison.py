
class Vehiculo:
    def __init__(self, tipo, velocidad):
        self.tipo = tipo
        self.velocidad = velocidad
    def obtener_velocidad(self):
        return self.velocidad

yeison_david_moreno_nieto = Vehiculo("Moto", 80)
print(yeison_david_moreno_nieto.obtener_velocidad())


