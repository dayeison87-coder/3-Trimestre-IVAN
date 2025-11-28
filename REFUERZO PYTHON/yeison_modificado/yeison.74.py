

class Plato:
    def __init__(self, nombre, precio):
        self.nombre = nombre
        self.precio = precio

class Restaurante:
    def __init__(self):
        self.menu = []

    def agregar_plato(self, plato):
        self.menu.append(plato)

yeison_david_moreno = Plato("Pizza", 20)
mi_restaurante = Restaurante()
mi_restaurante.agregar_plato(yeison_david_moreno)
for plato in mi_restaurante.menu:
    print(plato.nombre, plato.precio)




class Alumno:
    def __init__(self, nombre):
        self.nombre = nombre
    def mostrar_materias(self, materias):
        for m in materias:
            print(f"{self.nombre} estudia {m}")

yeison_david_moreno = Alumno("yeison david moreno")
yeison_david_moreno.mostrar_materias(["Matemáticas", "Física"])