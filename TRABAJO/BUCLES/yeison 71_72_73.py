#EJERCICIO 71
frase_david = input("Frase: ")
palabras_yeison = frase_david.split()
print("Cantidad de palabras:", len(palabras_yeison))



#EJERCICIO 72
notas_moreno = [3.5, 4.0, 2.8, 4.5]
suma_yeison = 0
for nota_nieto in notas_moreno:
    suma_yeison += nota_nieto
promedio_david = suma_yeison / len(notas_moreno)
print("Promedio:", promedio_david)


#EJERCICIO 73
for yeison in range(1, 11):
    doble_moreno = yeison * 2
    print(doble_moreno)
