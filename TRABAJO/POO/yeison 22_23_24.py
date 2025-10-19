#ejercicio 22
class PersonaMoreno:
    def __init__(self):
        self.nombre = "Yeison"
        self.edad = 20

    def mostrar(self):
        print(f"{self.nombre} tiene {self.edad} años")

nieto = PersonaMoreno()
nieto.mostrar()



#ejercicio 23
class ListaNombresDavid:
    def __init__(self):
        self.nombres = []

    def agregar_nombre(self, nombre):
        self.nombres.append(nombre)

    def mostrar_nombres(self):
        print("Lista de nombres:", self.nombres)

yeison = ListaNombresDavid()
yeison.agregar_nombre("Moreno")
yeison.agregar_nombre("Nieto")
yeison.mostrar_nombres()



#ejercicio 24
class NotaYeison:
    def evaluar(self, nota):
        if nota >= 3:
            print("Aprobado, Yeison!")
        else:
            print("Reprobado, David!")

moreno = NotaYeison()
moreno.evaluar(4)
