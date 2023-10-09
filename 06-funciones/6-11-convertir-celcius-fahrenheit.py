"""
Para convertir de ºC a ºF use la fórmula:   ºF = ºC x 1.8 + 32.
Para convertir de ºF a ºC use la fórmula:   ºC = (ºF-32) ÷ 1.8.
"""


def calcularFahrenheit(celcius):
    return celcius * 1.8 + 32


def calcularCelcius(fahrenheit):
    return (fahrenheit - 32) / 1.8


grados_celcius = float(input("Ingrese grados celcius:   "))
grados_fahrenheit = float(input("Ingrese grados fahrenheit:   "))

con_fahrenheit = calcularFahrenheit(grados_celcius)
con_celcius = calcularCelcius(grados_fahrenheit)


print(f"Celcius: {grados_celcius} = Fahrenheit: {con_fahrenheit}")
print(f"Fahrenheit: {grados_fahrenheit} = Celcius: {con_celcius}")
