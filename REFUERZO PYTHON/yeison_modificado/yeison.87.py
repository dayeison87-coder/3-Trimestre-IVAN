

class Estudiante:
    def __init__(self, nombre, notas):
        self.nombre = nombre
        self.notas = notas
    def promedio(self):
        return sum(self.notas) / len(self.notas)

yeison_david_moreno = Estudiante("yeison david moreno", [80, 90, 70])
print(yeison_david_moreno.promedio())


class Libro:
    def __init__(self, titulo, autor):
        self.titulo = titulo
        self.autor = autor

class Biblioteca:
    def __init__(self):
        self.libros = []
    def agregar_libro(self, libro):
        self.libros.append(libro)
    def filtrar_por_autor(self, autor):
        return [l.titulo for l in self.libros if l.autor == autor]

yeison_david_moreno = Libro("Python Avanzado", "yeison david moreno")
biblioteca = Biblioteca()
biblioteca.agregar_libro(yeison_david_moreno)
print(biblioteca.filtrar_por_autor("yeison david moreno"))