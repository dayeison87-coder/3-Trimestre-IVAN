class Animal(ABC):
    @abstractmethod
    def sonido(self):
        pass

class Gato(Animal):
    def sonido(self):
        print("Miau")

yeison_david_moreno_nieto = Gato()
yeison_david_moreno_nieto.sonido()