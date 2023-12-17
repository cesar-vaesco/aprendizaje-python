numeros = [1, 2, 3]
print(numeros)

print(*numeros)
print(*numeros, sep=" - ")


#  Desempaquetando al momento de parar un parámetro a una función
def sumar(a, b, c):
    return f"Resultado suma: {a + b + c}"


print(sumar(*numeros))

# Extraer algunos elemento de una lista

mi_lista = [1, 2, 3, 4, 5, 6]

a, *b, c, d = mi_lista

print(mi_lista)
print(a, b, c, d)
