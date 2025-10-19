#EJERCICIO 28
numero_moreno = input("Número: ")
suma_nieto = 0
for digito_yeison in numero_moreno:
    suma_nieto += int(digito_yeison)
print("Suma de dígitos:", suma_nieto)



#EJERCICIO 29
numero_david = input("Número: ")
invertido_yeison = numero_david[::-1]
print("Invertido:", invertido_yeison)


#EJERCICIO 30
palabra_moreno = input("Palabra: ").lower()
vocales_nieto = 0
for letra_yeison in palabra_moreno:
    if letra_yeison in "aeiou":
        vocales_nieto += 1
print("Cantidad de vocales:", vocales_nieto)
