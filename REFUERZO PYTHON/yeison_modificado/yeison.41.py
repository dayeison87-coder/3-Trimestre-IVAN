

def invertir_palabras_lista(yeison_david_moreno_lista):
    return [p[::-1] for p in yeison_david_moreno_lista]

print(invertir_palabras_lista(["yeison","moreno","nieto"]))


def ordenar_por_longitud(yeison_david_moreno_lista):
    return sorted(yeison_david_moreno_lista, key=len)

print(ordenar_por_longitud(["moreno","nieto","moreno"]))