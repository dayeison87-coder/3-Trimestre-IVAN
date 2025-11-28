

class Vehiculo:
    def __init__(self, marca, modelo):
        self.marca = marca
        self.modelo = modelo
    def info(self):
        print(f"Vehículo: {self.marca} {self.modelo}")

yeison_david_moreno = Vehiculo("Toyota", "Corolla")
yeison_david_moreno.info()



class Vehiculo:
    def info(self):
        print("Soy un vehículo")

class Auto(Vehiculo):
    def info(self):
        print("Soy un auto")

yeison_david_moreno = Auto()
yeison_david_moreno.info()
