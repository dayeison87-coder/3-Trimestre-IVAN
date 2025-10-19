def func28(lst):
    yeison = []
    for x in lst:
        if x not in yeison:
            yeison.append(x)
    return yeison

def func29(s):
    david = ''.join(ch for ch in s if ch.isalpha())
    return david

def func30(lst):
    moreno = sorted(lst)
    return moreno

