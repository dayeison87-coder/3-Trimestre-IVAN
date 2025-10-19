#ejercicio 52
class ParesDavid:
    def mostrar_pares(self, limite):
        for i in range(2, limite + 1, 2):
            print(i)

yeison = ParesDavid()
yeison.mostrar_pares(10)



#ejercicio 53
class FiltroMoreno:
    def filtrar_mayores(self, lista):
        return [n for n in lista if n > 10]

nieto = FiltroMoreno()
print(nieto.filtrar_mayores([5, 12, 8, 15, 3]))



#ejercicio 54
class FactorialYeison:
    def calcular(self, n):
        resultado = 1
        for i in range(1, n+1):
            resultado *= i
        return resultado

david = FactorialYeison()
print(david.calcular(5))
