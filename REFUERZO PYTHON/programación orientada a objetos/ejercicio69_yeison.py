class Alumno:
    def __init__(self, nombre):
        self.nombre = nombre
    def mostrar_materias(self, materias):
        for m in materias:
            print(f"{self.nombre} estudia {m}")

yeison_david_moreno_nieto = Alumno("Yeison David Moreno Nieto")
yeison_david_moreno_nieto.mostrar_materias(["Matemáticas", "Física"])