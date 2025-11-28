

def reemplazar_vocales(yeison_david_moreno_texto):
    return ''.join('*' if c.lower() in "aeiou" else c for c in yeison_david_moreno_texto)

print(reemplazar_vocales("yeison moreno nieto"))



def contar_palabras_letra(yeison_david_moreno_lista, yeison_david_moreno_letra):
    return len([p for p in yeison_david_moreno_lista if yeison_david_moreno_letra in p])

print(contar_palabras_letra(["yeison","moreno","nieto"], "a"))