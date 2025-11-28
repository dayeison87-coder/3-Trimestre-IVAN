

def lista_mayusculas(yeison_david_moreno_lista):
    return [x.upper() for x in yeison_david_moreno_lista]

print(lista_mayusculas(["hola","mundo"]))



def lista_tuplas_cuadrado(yeison_david_moreno_n):
    return [(x, x**2) for x in range(1, yeison_david_moreno_n+1)]

print(lista_tuplas_cuadrado(5))