

def mayusculas_filtradas(yeison_david_moreno_lista, yeison_david_moreno_letra):
    return [p.upper() for p in yeison_david_moreno_lista if p.startswith(yeison_david_moreno_letra)]

print(mayusculas_filtradas(["yeison","moreno","nieto"], "K"))


def contar_digitos(yeison_david_moreno_texto):
    return sum(1 for c in yeison_david_moreno_texto if c.isdigit())

print(contar_digitos("yeisonmoreno456"))