

class Libro:
    def __init__(self, titulo):
        self.titulo = titulo

class Biblioteca:
    def __init__(self):
        self.libros = []
    def agregar_libro(self, libro):
        self.libros.append(libro)
    def listar_libros(self):
        return [l.titulo for l in self.libros]

yeison_david_moreno = Libro("Python Básico")
mi_biblioteca = Biblioteca()
mi_biblioteca.agregar_libro(yeison_david_moreno)
print(mi_biblioteca.listar_libros())


class Contraseña:
    def __init__(self, clave):
        self.__clave = clave
    def mostrar_clave(self):
        print(self.__clave)

yeison_david_moreno = Contraseña("12345")
yeison_david_moreno.mostrar_clave()