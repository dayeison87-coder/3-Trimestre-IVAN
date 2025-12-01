

class Persona:
    def __init__(self, nombre):
        self.nombre = nombre

class Estudiante(Persona):
    def estudiar(self):
        print(f"{self.nombre} está estudiando")

yeison_david_moreno_nieto = Estudiante("Yeison David Moreno Nieto")
yeison_david_moreno_nieto.estudiar()


