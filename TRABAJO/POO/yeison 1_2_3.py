#EJERCICIO 1
class PersonaYeison:
    def saludar(self):
        print("Hola, soy una persona llamada Yeison.")

p1 = PersonaYeison()
p1.saludar()



#EJERCICIO 2
class PersonaDavid:
    def __init__(self, nombre):
        self.nombre = nombre

    def saludar(self):
        print(f"Hola, soy {self.nombre}")

moreno = PersonaDavid("Yeison David")
moreno.saludar()



#EJERCICIO 3
class MotoMoreno:
    def __init__(self, marca, modelo):
        self.marca = marca
        self.modelo = modelo

    def mostrar_info(self):
        print(f"Moto {self.marca} modelo {self.modelo}")

moto_nieto = MotoMoreno("Voge", "300DS")
moto_nieto.mostrar_info()
