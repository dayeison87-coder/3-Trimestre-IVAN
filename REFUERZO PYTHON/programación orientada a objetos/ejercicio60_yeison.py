class Alumno:
    def __init__(self, nombre):
        self.nombre = nombre
        self.asistencias = 0
    def registrar_asistencia(self):
        self.asistencias += 1

yeison_david_moreno_nieto = Alumno("Yeison David Moreno Nieto")
yeison_david_moreno_nieto.registrar_asistencia()
print(yeison_david_moreno_nieto.asistencias)