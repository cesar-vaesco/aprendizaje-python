from FiguraGeometrica import FiguraGeometrica
from Color import Color


class Rectangulo(FiguraGeometrica, Color):
    def __init__(self, alto, ancho, color):
        # super.__init__(lado)
        FiguraGeometrica.__init__(self, alto, ancho)
        Color.__init__(self, color)

    def calcular_area(self):
        return self.alto * self.ancho

    def __str__(self):
        return f"Rectangulo: {FiguraGeometrica.__str__(self)} {Color.__str__(self)}"


if __name__ == "__main__":
    rec1 = Rectangulo(12, 5, "Azul")

    print(rec1)
    print(rec1.calcular_area())
