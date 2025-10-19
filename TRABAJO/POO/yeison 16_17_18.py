#ejercicio 16
class ContadorYeison:
    total = 0

    @classmethod
    def aumentar(cls):
        cls.total += 1

ContadorYeison.aumentar()
ContadorYeison.aumentar()
print("Total:", ContadorYeison.total)



#ejercicio 17
class SaludoDavid:
    def mensaje(self):
        return "Hola, Yeison David Moreno Nieto!"

s = SaludoDavid()
print(s.mensaje())



#ejercicio 18
class PersonaNieto:
    def __init__(self, nombre):
        self.nombre = nombre

    def __str__(self):
        return f"Persona: {self.nombre}"

p = PersonaNieto("Yeison")
print(p)
