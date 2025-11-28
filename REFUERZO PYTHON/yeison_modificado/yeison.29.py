

def crear_sumador(yeison_david_moreno_n):
    def sumador(yeison_david_moreno_x):
        return yeison_david_moreno_n + yeison_david_moreno_x
    return sumador

sumar_5 = crear_sumador(5)
print(sumar_5(10))




def palabras_vocal_inicial(yeison_david_moreno_lista):
    return [p for p in yeison_david_moreno_lista if p[0].lower() in "aeiou"]

print(palabras_vocal_inicial(["Kevin","Ana","Oscar","Santiago"]))