class Persona:
    def __init__(self, nombre):
        self.nombre = nombre
    def duplicar(self):
        return Persona(self.nombre + " Jr.")

yeison_david_moreno_nieto = Persona("Yeison David Moreno Nieto")
nuevo_yeison = yeison_david_moreno_nieto.duplicar()
print(nuevo_yeison.nombre)