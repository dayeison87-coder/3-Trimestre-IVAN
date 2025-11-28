

def suma_dicc_valores(yeison_david_moreno_lista_dicc, yeison_david_moreno_clave):
    return sum(d[yeison_david_moreno_clave] for d in yeison_david_moreno_lista_dicc)

print(suma_dicc_valores([{"a":10},{"a":20},{"a":5}], "a"))




def filtrar_valores_impares(yeison_david_moreno_dicc):
    return {k:v for k,v in yeison_david_moreno_dicc.items() if v%2!=0}

print(filtrar_valores_impares({"a":1,"b":2,"c":3}))