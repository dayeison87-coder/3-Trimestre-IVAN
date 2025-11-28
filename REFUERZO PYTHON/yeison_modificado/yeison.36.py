

def todas_iguales(yeison_david_moreno_lista):
    return all(x == yeison_david_moreno_lista[0] for x in yeison_david_moreno_lista)

print(todas_iguales(["yeison","yeison","yeison"]))


def contar_letra_lista(yeison_david_moreno_lista, yeison_david_moreno_letra):
    return sum(word.count(yeison_david_moreno_letra) for word in yeison_david_moreno_lista)

print(contar_letra_lista(["yeison","yeison","moreno"], "o"))