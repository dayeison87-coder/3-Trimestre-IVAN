

def promedio_dicc(yeison_david_moreno_dicc):
    if not yeison_david_moreno_dicc:
        return 0
    return sum(yeison_david_moreno_dicc.values()) / len(yeison_david_moreno_dicc)

print(promedio_dicc({"a":10,"b":20}))



def claves_mayores(yeison_david_moreno_dicc, yeison_david_moreno_valor):
    return [k for k,v in yeison_david_moreno_dicc.items() if v > yeison_david_moreno_valor]

print(claves_mayores({"a":5,"b":10,"c":15}, 7))