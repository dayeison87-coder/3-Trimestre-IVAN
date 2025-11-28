

def filtrar_diccionario(yeison_david_moreno_dicc, yeison_david_moreno_valor):
    return {k:v for k,v in yeison_david_moreno_dicc.items() if v > yeison_david_moreno_valor}

print(filtrar_diccionario({"a":10,"b":20,"c":5}, 8))


def reemplazar_lista(yeison_david_moreno_lista, yeison_david_moreno_ant, yeison_david_moreno_nuev):
    return [x.replace(yeison_david_moreno_ant, yeison_david_moreno_nuev) for x in yeison_david_moreno_lista]

print(reemplazar_lista(["hola","hola mundo"], "hola","adios"))