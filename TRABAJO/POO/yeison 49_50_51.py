#ejercicio 49
class ListaYeison:
    def unir(self, lista):
        return " ".join(lista)

moreno = ListaYeison()
print(moreno.unir(["Hola", "David", "Moreno"]))



#ejercicio 50
class SumaNieto:
    def sumar_hasta(self, n):
        return sum(range(1, n+1))

david = SumaNieto()
print(david.sumar_hasta(10))




#ejercicio 51
class CuentaAtrasYeison:
    def contar(self, inicio):
        for i in range(inicio, 0, -1):
            print(i)

moreno = CuentaAtrasYeison()
moreno.contar(5)
