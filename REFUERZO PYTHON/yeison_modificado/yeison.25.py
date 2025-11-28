

def es_anagrama(yeison_david_moreno_1, yeison_david_moreno_2):
    return sorted(yeison_david_moreno_1.lower()) == sorted(yeison_david_moreno_2.lower())

print(es_anagrama("Roma", "Amor"))



def contar_mayores_listas(yeison_david_moreno_listas, yeison_david_moreno_valor):
    return [len([x for x in lst if x > yeison_david_moreno_valor]) for lst in yeison_david_moreno_listas]

print(contar_mayores_listas([[1,2,3],[4,5,6]], 3))