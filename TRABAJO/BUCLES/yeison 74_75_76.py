#EJERCICIO 74
for david in range(1, 101):
    if david % 9 == 0:
        print(david)



#EJERCICIO 75
for moreno in range(1, 6):
    cubo_yeison = moreno ** 3
    print(cubo_yeison)



#EJERCICIO 76
numeros_nieto = [1, 2, 3, 4, 5, 6]
pares_david = 0
for yeison in numeros_nieto:
    if yeison % 2 == 0:
        pares_david += 1
print("Cantidad de pares:", pares_david)
