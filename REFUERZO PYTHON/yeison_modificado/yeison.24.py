

def sumar_listas(yeison_david_moreno_listas):
    return [sum(lst) for lst in yeison_david_moreno_listas]

print(sumar_listas([[1,2,3],[4,5,6],[7,8]]))




def matriz_identidad(yeison_david_moreno_n):
    return [[1 if i==j else 0 for j in range(yeison_david_moreno_n)] for i in range(yeison_david_moreno_n)]

print(matriz_identidad(3))