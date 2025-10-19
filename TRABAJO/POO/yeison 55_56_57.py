#ejercicio 55
class NumeroMoreno:
    def es_primo(self, n):
        if n < 2:
            return False
        for i in range(2, int(n**0.5)+1):
            if n % i == 0:
                return False
        return True

yeison = NumeroMoreno()
print("¿Es primo?", yeison.es_primo(7))



#ejercicio 56
class NumeroNieto:
    def invertir(self, numero):
        return int(str(numero)[::-1])

david = NumeroNieto()
print(david.invertir(12345))




#ejercicio 57
class TextoYeison:
    def contar(self, texto):
        texto = texto.lower()
        vocales = sum(1 for l in texto if l in "aeiou")
        consonantes = sum(1 for l in texto if l.isalpha() and l not in "aeiou")
        return vocales, consonantes

moreno = TextoYeison()
print(moreno.contar("Yeison David"))
