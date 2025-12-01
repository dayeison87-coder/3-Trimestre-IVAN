class Persona:
    def __init__(self, nombre):
        self.nombre = nombre
    def __len__(self):
        return len(self.nombre)

yeison_david_moreno_nieto = Persona("Yeison David Moreno Nieto")
print(len(yeison_david_moreno_nieto))