class Rectangulo:
    def __init__(self, _base, _altura):
        self.base = _base
        self.altura = _altura

    def calcular_area(self):
        return self.base * self.altura

    def mostrarResultado(self):
        return f"El área del rectángulo es: {self.calcular_area()}"


base = int(input("Ingresa base del rectángulo:   "))
altura = int(input("Ingresa altura del rectángulo:   "))

rectangulo1 = Rectangulo(base, altura)

print(rectangulo1.mostrarResultado())
