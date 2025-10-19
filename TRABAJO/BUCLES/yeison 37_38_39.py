#EJERCICIO 37
numeros_david = [3, 4, 7, 8, 10]
for yeison in numeros_david:
    if yeison % 2 == 0:
        print(yeison)



#EJERCICIO 38
numeros_moreno = [3, 4, 7, 8, 10]
for david in numeros_moreno:
    if david % 2 != 0:
        print(david)



#EJERCICIO 39
numero_yeison = int(input("Número: "))
for moreno in range(1, numero_yeison + 1):
    if numero_yeison % moreno == 0:
        print(moreno)
