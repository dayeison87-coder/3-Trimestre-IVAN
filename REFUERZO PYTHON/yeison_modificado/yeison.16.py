
def promedio_diccionario(yeison_david_moreno_dicc):
    return sum(yeison_david_moreno_dicc.values()) / len(yeison_david_moreno_dicc)

print(promedio_diccionario({"a":10,"b":20,"c":30}))


def contar_palabras_largas(yeison_david_moreno_lista, yeison_david_moreno_n):
    return len([p for p in yeison_david_moreno_lista if len(p) > yeison_david_moreno_n])

print(contar_palabras_largas(["hola","adios","programacion"], 4))
