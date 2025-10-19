#ejercicio 37
class VocalesYeison:
    def contar(self, texto):
        contador = 0
        for letra in texto.lower():
            if letra in "aeiou":
                contador += 1
        return contador

moreno = VocalesYeison()
print(moreno.contar("David Moreno"))



#ejercicio 38
class RangoNieto:
    def generar(self, inicio, fin):
        return list(range(inicio, fin + 1))

david = RangoNieto()
print(david.generar(1, 5))



#ejercicio 39
class PersonaMoreno:
    def __init__(self, nombre):
        self.nombre = nombre

    def saludar(self):
        print(f"Hola, soy {self.nombre}")

class SaludoYeison:
    def presentar(self, persona):
        persona.saludar()

p = PersonaMoreno("David Nieto")
d = SaludoYeison()
d.presentar(p)
