class Persona:
    def __init__(self, nombre):
        self.nombre = nombre
    def crear_hijo(self):
        return Persona(self.nombre + " Jr.")

yeison_david_moreno_nieto = Persona("Yeison David Moreno Nieto")
hijo = yeison_david_moreno_nieto.crear_hijo()
print(hijo.nombre)