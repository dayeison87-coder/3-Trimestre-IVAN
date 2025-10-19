#ejercicio 98
class PalindromoYeison:
    def __init__(self, palabra_moreno):
        self.palabra_moreno = palabra_moreno.lower()

    def es_palindromo_david(self):
        if self.palabra_moreno == self.palabra_moreno[::-1]:
            print(f"La palabra '{self.palabra_moreno}' es un palíndromo.")
            return True
        else:
            print(f"La palabra '{self.palabra_moreno}' no es un palíndromo.")
            return False

texto_nieto = PalindromoYeison("Reconocer")
texto_nieto.es_palindromo_david()


#ejercicio 99
class FactorialDavid:
    def __init__(self, numero_yeison):
        self.numero_yeison = numero_yeison

    def calcular_factorial_moreno(self):
        factorial_nieto = 1
        for i_david in range(1, self.numero_yeison + 1):
            factorial_nieto *= i_david
        print(f"El factorial de {self.numero_yeison} es {factorial_nieto}")
        return factorial_nieto

num_moreno = FactorialDavid(5)
num_moreno.calcular_factorial_moreno()



#ejercicio 100
class TablaMultiplicarYeison:
    def __init__(self, numero_david):
        self.numero_david = numero_david

    def generar_tabla_moreno(self):
        print(f"Tabla de multiplicar del {self.numero_david}:")
        for i_nieto in range(1, 11):
            resultado_yeison = self.numero_david * i_nieto
            print(f"{self.numero_david} x {i_nieto} = {resultado_yeison}")

tabla_moreno = TablaMultiplicarYeison(7)
tabla_moreno.generar_tabla_moreno()
