#ejercicio 79
class TextoNieto:
    def contar_mayusculas(self, texto):
        return sum(1 for l in texto if l.isupper())

david = TextoNieto()
print(david.contar_mayusculas("Yeison David MORENO"))



#ejercicio 80
class PersonaYeison:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    def saludar(self):
        print(f"Hola, soy {self.nombre} y tengo {self.edad} años.")

class EstudianteDavid(PersonaYeison):
    def __init__(self, nombre, edad, curso):
        super().__init__(nombre, edad)
        self.curso = curso

    def mostrar(self):
        print(f"{self.nombre} ({self.edad} años) estudia {self.curso}")

moreno = EstudianteDavid("Yeison David Moreno Nieto", 22, "Programación")
moreno.saludar()
moreno.mostrar()



#ejercicio 81
# Ejercicio 61 - Creado por Yeison David Moreno Nieto
class VehiculoYeison:
    def __init__(self, marca_yeison, modelo_david):
        self.marca_yeison = marca_yeison
        self.modelo_david = modelo_david

auto_moreno = VehiculoYeison("Yamaha", "2025")
print("Marca:", auto_moreno.marca_yeison)
print("Modelo:", auto_moreno.modelo_david)
