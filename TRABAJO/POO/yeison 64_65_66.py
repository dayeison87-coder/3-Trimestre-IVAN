#ejercicion 64
class ListaYeison:
    def unir_listas(self, l1, l2):
        return l1 + l2

moreno = ListaYeison()
print(moreno.unir_listas([1,2], [3,4]))



#ejercicio 65
class PalabraDavid:
    def longitud(self, palabra):
        return len(palabra)

yeison = PalabraDavid()
print(yeison.longitud("Moreno"))



#ejercicio 66
class TextoNieto:
    def a_lista(self, texto):
        return list(texto)

moreno = TextoNieto()
print(moreno.a_lista("Yeison"))
