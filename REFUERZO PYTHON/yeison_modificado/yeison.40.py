

def palabras_largas_n(yeison_david_moreno_lista, yeison_david_moreno_n):
    return [p for p in yeison_david_moreno_lista if len(p) > yeison_david_moreno_n]

print(palabras_largas_n(["yeison","moreno","nieto"], 5))



def palabras_y_longitud(yeison_david_moreno_lista):
    return [(p,len(p)) for p in yeison_david_moreno_lista]

print(palabras_y_longitud(["yeison","moreno","nieto"]))