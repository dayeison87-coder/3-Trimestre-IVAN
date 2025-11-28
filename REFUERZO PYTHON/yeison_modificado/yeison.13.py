

def filtrar_palabras_letra(yeison_david_moreno_lista, yeison_david_moreno_letra):
    return [p for p in yeison_david_moreno_lista if yeison_david_moreno_letra in p]

print(filtrar_palabras_letra(["yeison","moreno","Carlos"], "a"))




def invertir_palabras(yeison_david_moreno_lista):
    return [p[::-1] for p in yeison_david_moreno_lista]

print(invertir_palabras(["yeison","moreno","Carlos"]))