

def es_palindromo(yeison_david_moreno):
    return yeison_david_moreno == yeison_david_moreno[::-1]

print(es_palindromo("ana"))



def filtrar_pares(yeison_david_moreno_lista):
    return [x for x in yeison_david_moreno_lista if x % 2 == 0]

print(filtrar_pares([1,2,3,4,5,6]))