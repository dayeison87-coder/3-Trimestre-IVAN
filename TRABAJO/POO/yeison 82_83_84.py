#ejercicio 82
class PersonaNieto:
    def __init__(self, nombre_yeison, edad_david):
        self.nombre_yeison = nombre_yeison
        self.edad_david = edad_david

    def saludar_moreno(self):
        print(f"Hola, soy {self.nombre_yeison} y tengo {self.edad_david} años")

p1 = PersonaNieto("Yeison", 20)
p1.saludar_moreno()


#ejercicio 83
class LibroYeison:
    def __init__(self, titulo_david):
        self.titulo_david = titulo_david

    def mostrar_nieto(self):
        print(f"El título del libro es {self.titulo_david}")

libro_moreno = LibroYeison("Python Fácil")
libro_moreno.mostrar_nieto()


#ejercicio 84
class EstudianteDavid:
    def __init__(self, nombre_moreno, nota_yeison):
        self.nombre_moreno = nombre_moreno
        self.nota_yeison = nota_yeison

    def aprobado_nieto(self):
        if self.nota_yeison >= 3.0:
            print(f"{self.nombre_moreno} aprobó con nota {self.nota_yeison}")
        else:
            print(f"{self.nombre_moreno} no aprobó, su nota fue {self.nota_yeison}")

estu_yeison = EstudianteDavid("David", 4.5)
estu_yeison.aprobado_nieto()
