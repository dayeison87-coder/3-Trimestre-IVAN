

def cuadrados_mayores_que(yeison_david_moreno_lista, yeison_david_moreno_n):
    return [x**2 for x in yeison_david_moreno_lista if x**2 > yeison_david_moreno_n]

print(cuadrados_mayores_que([1,2,3,4,5], 10))



def numeros_pares(yeison_david_moreno_inicio, yeison_david_moreno_fin):
    return [x for x in range(yeison_david_moreno_inicio, yeison_david_moreno_fin+1) if x%2==0]

print(numeros_pares(1,10))