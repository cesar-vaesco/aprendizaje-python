print(" Profundizando tuplas ".center(60, "*"))

# Declarar variables
a, b = "Hola", "Adios"
print(a, b)

# swap - intercambio
a, b = b, a
print(a, b)

print(" Regresando múltiples valores en una función ".center(60, "*"))


def minmax(elementos):
    return min(elementos), max(elementos)


min, max = minmax([1, 2, 3, 4, 5])
print(f"Valor minimo: {min} - Valor máximo: {max}")


print(" Regresar la suma de una tupla".center(60, "*"))
resultado = sum((1, 2, 3, 4, 5))
print(f"Resultado: {resultado}")


print(" Regresar la suma de una tupla a través de una función ".center(60, "*"))


def sumar(*args):
    return sum(args)


print(f"Resultado: {sumar(1, 2, 3, 4, 5)}")
