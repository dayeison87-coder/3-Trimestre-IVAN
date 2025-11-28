

def sumar_matrices(yeison_david_moreno_m1, yeison_david_moreno_m2):
    return [[yeison_david_moreno_m1[i][j] + yeison_david_moreno_m2[i][j] for j in range(len(yeison_david_moreno_m1[0]))] for i in range(len(yeison_david_moreno_m1))]

print(sumar_matrices([[1,2],[3,4]], [[5,6],[7,8]]))



def transponer_matriz(yeison_david_moreno_m):
    return [[yeison_david_moreno_m[j][i] for j in range(len(yeison_david_moreno_m))] for i in range(len(yeison_david_moreno_m[0]))]

print(transponer_matriz([[1,2,3],[4,5,6]]))