def func73(s):
    nieto = s[::-1]
    return nieto

def func74(n):
    yeison_david = 1
    i = 1
    while i<=n:
        yeison_david *= i
        i += 1
    return yeison_david

def func75(s):
    david_moreno = 0
    for ch in s:
        if ch.lower() in 'aeiou':
            david_moreno += 1
    return david_moreno

