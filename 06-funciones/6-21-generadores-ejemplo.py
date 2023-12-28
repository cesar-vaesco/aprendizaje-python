# Generador de números del 1 al 5


def generador_numeros():
    for numero in range(1, 6):
        yield numero
        print("Se reanudara la ejecución de la función ...")


# Utilizamos el objeto generador

generador = generador_numeros()

print(f"Objeto generador: {generador}")
print(f"Tipo objeto generador: {type(generador)}")

print("\n", " Recorrido generador ciclo For ".center(80, "*"))

for valor in generador:
    print(f"Número producido: {valor}")


generador = generador_numeros()
print("\n", " Impresión generador a demanda ".center(80, "*"), "\n")

try:
    print(f"Consumir a demanda: {next(generador)}")
    print(f"Consumir a demanda: {next(generador)}")
    print(f"Consumir a demanda: {next(generador)}")
    print(f"Consumir a demanda: {next(generador)}")
    print(f"Consumir a demanda: {next(generador)}")
    print(f"Consumir a demanda: {next(generador)}")
except StopIteration:
    print("\n\nError al consumir el generador\n\n")


print("\n", " Recorrido generador ciclo While ".center(80, "*"), "\n")
generador = generador_numeros()

try:
    while True:
        valor = next(generador)
        print(f"Impresión del valor generador: {valor} ")
except StopIteration as e:
    print("\n\nSe termino de iterar el generador\n\n")
