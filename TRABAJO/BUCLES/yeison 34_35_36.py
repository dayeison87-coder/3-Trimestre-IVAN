#EJERCICIO 34
for nieto in range(1, 101):
    if nieto % 3 == 0 and nieto % 5 == 0:
        print("FizzBuzz")
    elif nieto % 3 == 0:
        print("Fizz")
    elif nieto % 5 == 0:
        print("Buzz")
    else:
        print(nieto)



#EJERCICIO 35
suma_yeison = 0
numero_david = int(input("Número: "))
while numero_david != 0:
    suma_yeison += numero_david
    numero_david = int(input("Número: "))
print("Suma total:", suma_yeison)



#EJERCICIO 36
palabra_moreno = input("Palabra: ")
invertida_yeison = palabra_moreno[::-1]
print("Invertida:", invertida_yeison)
