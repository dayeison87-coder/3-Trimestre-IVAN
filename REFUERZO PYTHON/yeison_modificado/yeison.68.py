class Poligono:
    def __init__(self, lados):
        self.lados = lados

class Cuadrado(Poligono):
    def __init__(self, lado):
        super().__init__(4)
        self.lado = lado
    def area(self):
        return self.lado ** 2

yeison_david_moreno = Cuadrado(5)
print(yeison_david_moreno.area())




class Profesor:
    def __init__(self, nombre):
        self.nombre = nombre
        self.materias = []

    def agregar_materia(self, materia):
        self.materias.append(materia)

yeison_david_moreno = Profesor("yeison david moreno")
yeison_david_moreno.agregar_materia("Matemáticas")
print(yeison_david_moreno.materias)