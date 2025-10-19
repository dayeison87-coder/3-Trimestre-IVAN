#ejercicio 70
class TextoYeison:
    def contar_palabras(self, texto):
        return len(texto.split())

moreno = TextoYeison()
print(moreno.contar_palabras("Hola soy Yeison Moreno Nieto"))




#ejercicio 71
class NumeroMoreno:
    def convertir(self, numero):
        return str(numero)

david = NumeroMoreno()
print(type(david.convertir(100)))




#ejercicio 72
class MultiplicadorYeison:
    def multiplicar_lista(self, lista):
        resultado = 1
        for n in lista:
            resultado *= n
        return resultado

nieto = MultiplicadorYeison()
print(nieto.multiplicar_lista([2, 3, 4]))
