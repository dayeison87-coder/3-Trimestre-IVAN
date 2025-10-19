#EJERCICIO 65
texto_moreno = input("Texto: ")
for posicion_yeison in range(0, len(texto_moreno), 2):
    print(texto_moreno[posicion_yeison])



#EJERCICIO 66
lista_david = [2, 7, 4, 9, 10]
suma_yeison = 0
for numero_moreno in lista_david:
    if numero_moreno % 2 == 0:
        suma_yeison += numero_moreno
print("Suma pares:", suma_yeison)



#EJERCICIO 67
for nieto in range(1, 61):
    if nieto % 6 == 0:
        print(nieto)
