#ejercicio 91
class NotasYeison:
    def __init__(self, nota1_david, nota2_moreno, nota3_nieto):
        self.nota1_david = nota1_david
        self.nota2_moreno = nota2_moreno
        self.nota3_nieto = nota3_nieto

    def calcular_promedio_yeison(self):
        promedio = (self.nota1_david + self.nota2_moreno + self.nota3_nieto) / 3
        print(f"El promedio de Yeison David Moreno Nieto es: {promedio:.2f}")
        return promedio

notas_alumno = NotasYeison(4.0, 3.5, 4.5)
notas_alumno.calcular_promedio_yeison()


#ejercicio 92
class TemperaturaDavid:
    def __init__(self, celsius_yeison):
        self.celsius_yeison = celsius_yeison

    def convertir_a_fahrenheit_moreno(self):
        fahrenheit_nieto = (self.celsius_yeison * 9/5) + 32
        print(f"{self.celsius_yeison}°C equivalen a {fahrenheit_nieto}°F")
        return fahrenheit_nieto

temp_yeison = TemperaturaDavid(25)
temp_yeison.convertir_a_fahrenheit_moreno()



#ejercicio 93
class ContadorVocalesYeison:
    def __init__(self, palabra_david):
        self.palabra_david = palabra_david.lower()

    def contar_vocales_moreno(self):
        contador_nieto = 0
        for letra_yeison in self.palabra_david:
            if letra_yeison in "aeiou":
                contador_nieto += 1
        print(f"La palabra '{self.palabra_david}' tiene {contador_nieto} vocales.")
        return contador_nieto

palabra_yeison = ContadorVocalesYeison("Programacion")
palabra_yeison.contar_vocales_moreno()
