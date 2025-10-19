#ejercicio 92
producto_david = 1
for moreno in range(1, 6):
    producto_david *= moreno
print("Producto:", producto_david)


#ejercicio 93
frase_nieto = input("Frase: ")
espacios_yeison = 0
for caracter_david in frase_nieto:
    if caracter_david == " ":
        espacios_yeison += 1
print("Espacios:", espacios_yeison)



#ejercicio 94
for moreno in range(1, 11):
    print(moreno, moreno ** 2)
