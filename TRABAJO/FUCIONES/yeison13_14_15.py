def func13(s):
    moreno_nieto = s[::-1]
    return moreno_nieto

def func14(n):
    yeison = 1
    i = 1
    while i<=n:
        yeison *= i
        i += 1
    return yeison

def func15(s):
    david = 0
    for ch in s:
        if ch.lower() in 'aeiou':
            david += 1
    return david

