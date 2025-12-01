class Vehiculo:
    def __init__(self, tipo, velocidad):
        self.tipo = tipo
        self.velocidad = velocidad
    def acelerar(self, aumento):
        self.velocidad += aumento

yeison_david_moreno_nieto = Vehiculo("Coche", 50)
yeison_david_moreno_nieto.acelerar(20)
print(yeison_david_moreno_nieto.velocidad)