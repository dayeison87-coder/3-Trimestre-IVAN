def func97(a,b):
    x = a
    y = b
    while y:
        x,y = y,x%y
    moreno_nieto = x
    return moreno_nieto

def func98(lst):
    yeison = []
    for x in lst:
        if x not in yeison:
            yeison.append(x)
    return yeison

def func99(s):
    david = ''.join(ch for ch in s if ch.isalpha())
    return david

