

def lista_cuadrados(yeison_david_moreno_n):
    return [x**2 for x in range(1, yeison_david_moreno_n+1)]

print(lista_cuadrados(5))


def en_rango(yeison_david_moreno_num, yeison_david_moreno_min, yeison_david_moreno_max):
    return yeison_david_moreno_min <= yeison_david_moreno_num <= yeison_david_moreno_max

print(en_rango(5, 1, 10))