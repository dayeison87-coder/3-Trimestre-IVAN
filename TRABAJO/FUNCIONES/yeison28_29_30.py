# Ejercicio 1
def func28(lst):
    yeison = []
    for x in lst:
        if x not in yeison:
            yeison.append(x)
    return yeison

# Ejercicio 2
def func29(s):
    david = ''.join(ch for ch in s if ch.isalpha())
    return david

# Ejercicio 3
def func30(lst):
    moreno = sorted(lst)
    return moreno

