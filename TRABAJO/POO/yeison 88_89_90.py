#ejercicio 88
class CocheDavid:
    def __init__(self, color_yeison):
        self.color_yeison = color_yeison

    def pintar_moreno(self, nuevo_color):
        print(f"El coche cambia de color {self.color_yeison} a {nuevo_color}")
        self.color_yeison = nuevo_color

auto_yeison = CocheDavid("Rojo")
auto_yeison.pintar_moreno("Negro")
print(f"Color final del coche: {auto_yeison.color_yeison}")



#ejercicio 89
class RectanguloYeison:
    def __init__(self, ancho_david, alto_moreno):
        self.ancho_david = ancho_david
        self.alto_moreno = alto_moreno

    def calcular_area_nieto(self):
        area = self.ancho_david * self.alto_moreno
        print(f"El área del rectángulo es: {area}")
        return area

rect_yeison = RectanguloYeison(10, 5)
rect_yeison.calcular_area_nieto()


#ejercicio 90
class EstudianteMoreno:
    def __init__(self, nombre_yeison, edad_david):
        self.nombre_yeison = nombre_yeison
        self.edad_david = edad_david

    def mostrar_informacion_nieto(self):
        print(f"Nombre del estudiante: {self.nombre_yeison}, Edad: {self.edad_david}")

alumno_david = EstudianteMoreno("Yeison Moreno", 22)
alumno_david.mostrar_informacion_nieto()




