def func25(s):
    yeison_david = 0
    for ch in s:
        if ch.lower() in 'aeiou':
            yeison_david += 1
    return yeison_david

def func26(n):
    a,b = 0,1
    i = 0
    while i<n:
        a,b = b,a+b
        i += 1
    david_moreno = a
    return david_moreno

def func27(a,b):
    x = a
    y = b
    while y:
        x,y = y,x%y
    moreno_nieto = x
    return moreno_nieto

