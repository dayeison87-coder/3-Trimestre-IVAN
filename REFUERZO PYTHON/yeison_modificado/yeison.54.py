 

class Utilidades:
    @staticmethod
    def sumar(a, b):
        return a + b

    contador = 0
    @classmethod
    def incrementar_contador(cls):
        cls.contador += 1
        return cls.contador

print(Utilidades.sumar(5, 10))
print(Utilidades.incrementar_contador())
 

class Animal:
    def sonido(self):
        print("Hace un sonido")

class Perro(Animal):
    def sonido(self):
        print("Guau!")

yeison_david_moreno = Perro()
yeison_david_moreno.sonido()
