#ejercicio 85
class AnimalYeison:
    def sonido(self):
        print("Sonido genérico de animal")

class PerroDavid(AnimalYeison):
    def sonido(self):
        print("Guau Guau, soy un perro llamado Yeison")

perro_nieto = PerroDavid()
perro_nieto.sonido()



#ejercicio 86
class CalculadoraMoreno:
    def sumar_yeison(self, a, b):
        resultado = a + b
        print(f"{a} + {b} = {resultado}")
        return resultado

    def restar_david(self, a, b):
        resultado = a - b
        print(f"{a} - {b} = {resultado}")
        return resultado

calc_nieto = CalculadoraMoreno()
calc_nieto.sumar_yeison(10, 5)
calc_nieto.restar_david(10, 5)



#ejercicio 87}
class CuentaBancariaYeison:
    def __init__(self, titular_moreno, saldo_david=0):
        self.titular_moreno = titular_moreno
        self.saldo_david = saldo_david

    def depositar_yeison(self, monto):
        self.saldo_david += monto
        print(f"Depósito de {monto} realizado. Nuevo saldo: {self.saldo_david}")

    def retirar_nieto(self, monto):
        if monto <= self.saldo_david:
            self.saldo_david -= monto
            print(f"Retiro de {monto} realizado. Saldo restante: {self.saldo_david}")
        else:
            print("Fondos insuficientes")

    def mostrar_saldo(self):
        print(f"Saldo actual de {self.titular_moreno}: {self.saldo_david}")

cuenta_nieto = CuentaBancariaYeison("Yeison", 1000)
cuenta_nieto.depositar_yeison(500)
cuenta_nieto.retirar_nieto(300)
cuenta_nieto.mostrar_saldo()




