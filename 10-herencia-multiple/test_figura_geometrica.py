from Cuadrado import Cuadrado
from FiguraGeometrica import FiguraGeometrica
from Rectangulo import Rectangulo

fig = FiguraGeometrica(1, 1)

cuadrado1 = Cuadrado(lado=5, color="Rojo")
rectangulo1 = Rectangulo(alto=9, ancho=5, color="Azul")


# print(cuadrado1._alto)
# print(cuadrado1._ancho)
# print(cuadrado1._color)
# print(cuadrado1.calcular_area())

print(" Creación objeto cuadrado ".center(50, "-"))
print(cuadrado1)
print(f"Calculo del área cuadrado: {cuadrado1.calcular_area()}")
print(" Creación objeto rectángulo ".center(50, "-"))
print(rectangulo1)
print(f"Calculo del área réctangulo: {rectangulo1.calcular_area()}")
