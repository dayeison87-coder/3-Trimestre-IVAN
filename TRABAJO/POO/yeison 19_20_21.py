#ejercicio 19}
class TextoMoreno:
    def contar_caracteres(self, texto):
        return len(texto)

t = TextoMoreno()
print("Cantidad:", t.contar_caracteres("Yeison"))



#ejercicio 20
class PalabraYeison:
    def invertir(self, palabra):
        return palabra[::-1]

david = PalabraYeison()
print(david.invertir("moreno"))



#ejercicio 21
class CalculadoraYeison:
    def doble(self, numero):
        return numero * 2

david = CalculadoraYeison()
print(david.doble(10))
