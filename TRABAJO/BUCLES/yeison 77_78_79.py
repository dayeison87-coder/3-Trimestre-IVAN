#EJERCICIO 77
frase_moreno = input("Frase: ")
contador_yeison = 0
for letra_david in frase_moreno:
    contador_yeison += 1
print("Caracteres:", contador_yeison)



#EJERCICIO 78
numero_nieto = int(input("Número: "))
for yeison in range(1, numero_nieto + 1):
    if numero_nieto % yeison == 0:
        print(yeison)



#EJERCICIO 79
suma_david = 0
for moreno in range(1, 101):
    suma_david += moreno
print("Suma total:", suma_david)
