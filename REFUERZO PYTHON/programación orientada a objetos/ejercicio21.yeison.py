

class Persona:
    def actividad(self):
        print("actuando como persona")

class Profesor(Persona):
    def actividad(self):
        print("pensando en la clase")

yeison_david_moreno_nieto = Profesor()
yeison_david_moreno_nieto.actividad()


