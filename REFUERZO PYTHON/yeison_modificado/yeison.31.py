

def caracteres_unicos(yeison_david_moreno_texto):
    return len(set(yeison_david_moreno_texto))

print(caracteres_unicos("yeison moreno"))




def primeros_primos(yeison_david_moreno_n):
    primos = []
    num = 2
    while len(primos) < yeison_david_moreno_n:
        if all(num % x != 0 for x in range(2,num)):
            primos.append(num)
        num += 1
    return primos

print(primeros_primos(5))