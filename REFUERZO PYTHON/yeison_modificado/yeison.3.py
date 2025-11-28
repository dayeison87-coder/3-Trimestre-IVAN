

def frecuencia(yeison_david_moreno_lista):
    freq = {}
    for x in yeison_david_moreno_lista:
        freq[x] = freq.get(x, 0) + 1
    return freq

print(frecuencia([1,2,2,3,3,3]))



def lista_pares(yeison_david_moreno_n):
    return [x for x in range(1, yeison_david_moreno_n+1) if x % 2 == 0]

print(lista_pares(10))