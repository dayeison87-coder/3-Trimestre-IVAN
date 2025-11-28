
def contar_vocales(yeison_david_moreno):
    return sum(1 for c in yeison_david_moreno.lower() if c in "aeiou")

print(contar_vocales("yeison moreno"))




def promedio(yeison_david_moreno_lista):
    return sum(yeison_david_moreno_lista) / len(yeison_david_moreno_lista)

print(promedio([10, 20, 30]))