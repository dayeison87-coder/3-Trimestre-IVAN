#EJERCICIO 31
palabra_david = input("Palabra: ").lower()
consonantes_moreno = 0
for letra_yeison in palabra_david:
    if letra_yeison.isalpha() and letra_yeison not in "aeiou":
        consonantes_moreno += 1
print("Consonantes:", consonantes_moreno)



#EJERCICIO 32
for yeison in range(1, 101):
    if yeison % 3 == 0:
        print("Fizz")
    else:
        print(yeison)



#EJERCICIO 33
for moreno in range(1, 101):
    if moreno % 5 == 0:
        print("Buzz")
    else:
        print(moreno)
