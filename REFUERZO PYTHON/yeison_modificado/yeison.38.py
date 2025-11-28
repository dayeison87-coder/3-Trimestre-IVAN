

def concatenar_palabras(yeison_david_moreno_lista, yeison_david_moreno_separador="-"):
    return yeison_david_moreno_separador.join(yeison_david_moreno_lista)

print(concatenar_palabras(["yeison","moreno","nieto"]))
print(concatenar_palabras(["yeison","moreno","nieto"], " "))



def contar_vocales_lista(yeison_david_moreno_lista):
    return [sum(1 for c in p.lower() if c in "aeiou") for p in yeison_david_moreno_lista]

print(contar_vocales_lista(["yeison","moreno","nieto"]))