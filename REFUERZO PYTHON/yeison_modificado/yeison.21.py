
def divisores(yeison_david_moreno_num):
    return [x for x in range(1, yeison_david_moreno_num+1) if yeison_david_moreno_num % x == 0]

print(divisores(12))



def palabras_unicas(yeison_david_moreno_lista):
    return len(set(yeison_david_moreno_lista))

print(palabras_unicas(["hola","mundo","hola"]))