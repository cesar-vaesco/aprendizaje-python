valores = 1, 2, 3

print(type(valores))
print(valores)

valor1, valor2, valor3 = 1, 2, 3

print(valor1, valor2, valor3)

valor1, _, valor3 = 1, 2, 3

print(valor1, valor3)

valor1, valor2, *valor3 = 1, 2, 3, 4, 5, 6, 7, 8, 9

print(valor1, valor2, valor3)

print(type(valor3))

valor1, valor2, *valor3, valor8, valor9 = 1, 2, 3, 4, 5, 6, 7, 8, 9

print(valor1, valor2, valor3, valor8, valor9)

print(type(valor3))

print(valor3[4])

valor1, valor2, *valor3, valor8, valor9 = [1, 2, 3, 4, 5, 6, 7, 8, 9]

print(valor1, valor2, valor3, valor8, valor9)
print(type(valor3))


def regresar_varios_datos():
    return 1, 2, 3


valor1, valor2, valor3 = regresar_varios_datos()
print(valor1, valor2, valor3)

valor1, *valores_restantes = regresar_varios_datos()
print(valor1, valores_restantes)


# help(str.partition)
hora, separador, minutos = "17:20".partition(":")
print(hora, separador, minutos)
