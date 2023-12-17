numeros = [1, 2, 3]
print(numeros)

print(*numeros)
print(*numeros, sep=" - ")


#  Desempaquetando al momento de parar un parámetro a una función
def sumar(a, b, c):
    return f"Resultado suma: {a + b + c}"


print(sumar(*numeros))
