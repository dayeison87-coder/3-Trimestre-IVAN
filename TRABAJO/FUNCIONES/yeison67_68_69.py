# Ejercicio 1
def func67(a,b):
    x = a
    y = b
    while y:
        x,y = y,x%y
    yeison_david = x
    return yeison_david

# Ejercicio 2
def func68(lst):
    david_moreno = []
    for x in lst:
        if x not in david_moreno:
            david_moreno.append(x)
    return david_moreno

# Ejercicio 3
def func69(s):
    moreno_nieto = ''.join(ch for ch in s if ch.isalpha())
    return moreno_nieto

