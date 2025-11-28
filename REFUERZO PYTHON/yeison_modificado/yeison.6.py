

def dict_cuadrados(yeison_david_moreno_n):
    return {x: x**2 for x in range(1, yeison_david_moreno_n+1)}

print(dict_cuadrados(5))



def mayores_que(yeison_david_moreno_lista, yeison_david_moreno_valor):
    return [x for x in yeison_david_moreno_lista if x > yeison_david_moreno_valor]

print(mayores_que([1,5,10,2], 4))