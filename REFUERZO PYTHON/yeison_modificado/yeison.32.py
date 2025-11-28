

def factoriales_lista(yeison_david_moreno_n):
    def factorial(n):
        return 1 if n==0 else n*factorial(n-1)
    return [factorial(i) for i in range(yeison_david_moreno_n+1)]

print(factoriales_lista(5))



def contar_letras_lista(yeison_david_moreno_lista):
    return [len(p) for p in yeison_david_moreno_lista]

print(contar_letras_lista(["yeisno","moreno","nieto"]))