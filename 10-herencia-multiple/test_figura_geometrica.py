from Cuadrado import Cuadrado
from Rectangulo import Rectangulo

cuadrado1 = Cuadrado(lado=5, color="Rojo")
rectangulo1 = Rectangulo(alto=10, ancho=15, color="Azul")


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
