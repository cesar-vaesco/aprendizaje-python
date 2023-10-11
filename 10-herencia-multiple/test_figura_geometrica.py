from Cuadrado import Cuadrado
from Rectangulo import Rectangulo

cuadrado1 = Cuadrado(5, "Rojo")
rectangulo1 = Rectangulo(10, 15, "Azul")


# print(cuadrado1._alto)
# print(cuadrado1._ancho)
# print(cuadrado1._color)
# print(cuadrado1.calcular_area())

print(cuadrado1)
print(f"Calculo del área cuadrado: {cuadrado1.calcular_area()}")
print(rectangulo1)
print(f"Calculo del área réctangulo: {rectangulo1.calcular_area()}")
