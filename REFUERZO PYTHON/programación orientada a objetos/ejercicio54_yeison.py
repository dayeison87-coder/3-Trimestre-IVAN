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

yeison_david_moreno_nieto = Libro("Python Avanzado", "Yeison David Moreno Nieto")
biblioteca = Biblioteca()
biblioteca.agregar_libro(yeison_david_moreno_nieto)
print(biblioteca.filtrar_por_autor("Yeison David Moreno Nieto"))