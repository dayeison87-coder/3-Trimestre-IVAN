

def diccionario_indice(yeison_david_moreno_lista):
    return {i: yeison_david_moreno_lista[i] for i in range(len(yeison_david_moreno_lista))}

print(diccionario_indice(["a","b","c"]))




def sumar_pares_impares(yeison_david_moreno_lista):
    pares = sum(x for x in yeison_david_moreno_lista if x % 2 == 0)
    impares = sum(x for x in yeison_david_moreno_lista if x % 2 != 0)
    return pares, impares

print(sumar_pares_impares([1,2,3,4,5]))