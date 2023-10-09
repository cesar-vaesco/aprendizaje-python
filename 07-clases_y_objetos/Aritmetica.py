class Aritmetica:
    """
    Clase aritmrtica para realizar las operaciones de sumar, restar, etx

    """

    def __init__(self, _operandoA, _operandoB):
        self.operandoA = _operandoA
        self.operandoB = _operandoB

    def sumar(self):
        return self.operandoA + self.operandoB

    def restar(self):
        return self.operandoA - self.operandoB

    def multiplicar(self):
        return self.operandoA * self.operandoB

    def dividir(self):
        return self.operandoA / self.operandoB


operA = int(input("Ingresa primer digito: "))
operB = int(input("Ingresa segunfo digito: "))


aritmetica1 = Aritmetica(operA, operB)


print(f"Resultado de suma: {aritmetica1.sumar()}")
print(f"Resultado de resta: {aritmetica1.restar()}")
print(f"Resultado de multiplicación: {aritmetica1.multiplicar()}")
print(f"Resultado de división: {aritmetica1.dividir():.2f}")
