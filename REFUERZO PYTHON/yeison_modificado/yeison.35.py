

def filtrar_clave(yeison_david_moreno_dicc, yeison_david_moreno_clave):
    return {k:v for k,v in yeison_david_moreno_dicc.items() if yeison_david_moreno_clave in k}

print(filtrar_clave({"yeison":1,"moreno":2,"nieto":3}, "K"))



def divisibles_por(yeison_david_moreno_lista, yeison_david_moreno_n):
    return [x for x in yeison_david_moreno_lista if x % yeison_david_moreno_n == 0]

print(divisibles_por([1,2,3,4,5,6], 2))