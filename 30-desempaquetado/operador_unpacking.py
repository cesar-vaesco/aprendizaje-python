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


# unir listas
lista1 = [1, 2, 3]
lista2 = [4, 5, 6]

lista3 = [lista1, lista2]

print(f"Lista de listas: {lista3}")

lista3 = [*lista1, *lista2]
print(f"Unión de listas: {lista3}")

# Unir diccionarios
dic1 = {"A": 1, "B": 2, "C": 3}
dic2 = {"D": 4, "E": 5}

dic3 = {**dic1, **dic2}

print(f"Dic1: {dic1}")
print(f"Dic2: {dic2}")
print(f"Unión de diccionarios: {dic3}")

# Construir una lista a partir de un str

lista = [*"Hola Mundo"]
print(lista)
print(*lista)
print(*lista, sep="")
print(lista[8])
