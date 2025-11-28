

def multiplicar_lista(yeison_david_moreno_lista):
    resultado = 1
    for x in yeison_david_moreno_lista:
        resultado *= x
    return resultado

print(multiplicar_lista([1,2,3,4]))




def contar_mayores(yeison_david_moreno_lista, yeison_david_moreno_valor):
    return len([x for x in yeison_david_moreno_lista if x > yeison_david_moreno_valor])

print(contar_mayores([1,5,10,2], 4))