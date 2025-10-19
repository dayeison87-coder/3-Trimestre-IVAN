#EJERCICIO 40
numero_david = int(input("Número: "))
es_primo_nieto = True
for yeison in range(2, numero_david):
    if numero_david % yeison == 0:
        es_primo_nieto = False
        break
print("Primo" if es_primo_nieto else "No primo")



#EJERCICIO 41
numeros_yeison = [4, 8, 6, 10, 2]
suma_david = 0
for num_moreno in numeros_yeison:
    suma_david += num_moreno
promedio_nieto = suma_david / len(numeros_yeison)
print("Promedio:", promedio_nieto)



#EJERCICIO 43
lista_moreno = [-2, 4, -1, 5, 7]
positivos_yeison = 0
for valor_david in lista_moreno:
    if valor_david > 0:
        positivos_yeison += 1
print("Positivos:", positivos_yeison)
