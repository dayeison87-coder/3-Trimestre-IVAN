#EJERCICIO 47
palabra_yeison = input("Palabra: ")
contador_david = 0
for letra_moreno in palabra_yeison:
    contador_david += 1
print("Letras:", contador_david)



#EJERCICIO 48
frutas_nieto = ["manzana", "pera", "mango"]
for yeison in frutas_nieto:
    print(yeison)



#EJERCICIO 49
numero_david = input("Número: ")
suma_moreno = 0
for digito_yeison in numero_david:
    if int(digito_yeison) % 2 == 0:
        suma_moreno += int(digito_yeison)
print("Suma de dígitos pares:", suma_moreno)
