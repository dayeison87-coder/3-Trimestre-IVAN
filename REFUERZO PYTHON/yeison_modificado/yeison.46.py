
def pares_lista_anidada(yeison_david_moreno_listas):
    return [x for sublist in yeison_david_moreno_listas for x in sublist if x%2==0]

print(pares_lista_anidada([[1,2,3],[4,5,6]]))




def contar_palabra_lista(yeison_david_moreno_lista, yeison_david_moreno_palabra):
    return yeison_david_moreno_lista.count(yeison_david_moreno_palabra)

print(contar_palabra_lista(["yeison","morenno"], "yeison"))