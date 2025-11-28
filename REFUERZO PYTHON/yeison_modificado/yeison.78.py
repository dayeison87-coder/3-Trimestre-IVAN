

class Animal:
    def hablar(self):
        print("Algún sonido")

class Gato(Animal):
    def hablar(self):
        print("Miau")

yeison_david_moreno = Gato()
yeison_david_moreno.hablar()



class Nadador:
    def nadar(self):
        print("Nadando")

class Corredor:
    def correr(self):
        print("Corriendo")

class Atleta(Nadador, Corredor):
    pass

yeison_david_moreno = Atleta()
yeison_david_moreno.nadar()
yeison_david_moreno.correr()