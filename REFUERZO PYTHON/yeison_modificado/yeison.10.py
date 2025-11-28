

def promedio_lista(yeison_david_moreno_lista):
    if not yeison_david_moreno_lista:
        return "Lista vacía"
    return sum(yeison_david_moreno_lista) / len(yeison_david_moreno_lista)

print(promedio_lista([10,20,30]))
print(promedio_lista([]))




def buscar_elemento(yeison_david_moreno_lista, yeison_david_moreno_elemento):
    return yeison_david_moreno_elemento in yeison_david_moreno_lista

print(buscar_elemento([1,2,3], 2))