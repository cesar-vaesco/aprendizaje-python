"""
Generadores
- Es una función especial, retorna una secuencia de valores
- Suspende la ejecución  de la función yield (producir) (no se usara return)
"""


def generador():
    yield 1
    print("Se reanuda la ejecuón para entregar el siguiente valor")
    yield 2
    print("Se reanuda la ejecuón para entregar el siguiente valor")
    yield 3


# Se consume el generador a demanda
gen = generador()
# Con cada llamada consumimos un valor

print(f"Primer generador solicitado: {next(gen)}")

try:
    print(next(gen))
    print(next(gen))
    print(next(gen))
    print(next(gen))
except StopIteration:
    print(
        "\n",
        "Se ha lanzado un error StopIteration por tratar de consumir más valores de los que produce el generador",
    )

print("\n", " Consumiendo valores del generador con ciclo for ".center(60, "*"))

for valor in generador():
    print(f"Número generado: {valor}")
