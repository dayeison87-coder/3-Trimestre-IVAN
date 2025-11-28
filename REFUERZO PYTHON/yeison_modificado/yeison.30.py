

def cuadrados_pares(yeison_david_moreno_lista):
    return [x**2 for x in yeison_david_moreno_lista if x % 2 == 0]

print(cuadrados_pares([1,2,3,4,5]))



def tuplas_a_dicc(yeison_david_moreno_lista):
    return {k:v for k,v in yeison_david_moreno_lista}

print(tuplas_a_dicc([("a",1),("b",2)]))