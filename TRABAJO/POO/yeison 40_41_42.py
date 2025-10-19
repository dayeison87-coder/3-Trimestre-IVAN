#ejercicio 40
class PromedioYeison:
    def calcular(self, notas):
        return sum(notas) / len(notas)

moreno = PromedioYeison()
print("Promedio:", moreno.calcular([3.5, 4.0, 4.5]))



#ejercicio 41
class PalindromoYeison:
    def es_palindromo(self, palabra):
        palabra = palabra.lower().replace(" ", "")
        return palabra == palabra[::-1]

david = PalindromoYeison()
print(david.es_palindromo("anita lava la tina"))



#ejercicio 42
class TiempoMoreno:
    def segundos_a_minutos(self, segundos):
        return segundos / 60

nieto = TiempoMoreno()
print("Minutos:", nieto.segundos_a_minutos(180))
