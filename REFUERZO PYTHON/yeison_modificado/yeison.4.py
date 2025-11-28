
def palabras_con_inicial(yeison_david_moreno_lista, yeison_david_moreno_letra):
    return [p for p in yeison_david_moreno_lista if p.startswith(yeison_david_moreno_letra)]

print(palabras_con_inicial(["yeison","moreno","Carlos"], "K"))



def reemplazar_palabra(yeison_david_moreno_texto, yeison_david_moreno_antigua, yeison_david_moreno_nueva):
    return yeison_david_moreno_texto.replace(yeison_david_moreno_antigua, yeison_david_moreno_nueva)

print(reemplazar_palabra("Hola yeison", "moreno", "nieto"))