# Ejercicio 1
def func7(a,b):
    x = a
    y = b
    while y:
        x,y = y,x%y
    yeison = x
    return yeison

# Ejercicio 2
def func8(lst):
    david = []
    for x in lst:
        if x not in david:
            david.append(x)
    return david

# Ejercicio 3
def func9(s):
    moreno = ''.join(ch for ch in s if ch.isalpha())
    return moreno

