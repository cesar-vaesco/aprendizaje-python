# print(dir(__builtins__))
# help(zip)

numeros = [1, 2, 3]
numeros_tupla = (1, 2, 3)
letras = ["a", "b", "c", "d"]
identificadores = (
    321,
    322,
    323,
    324,
)
conjunto = {6, 4, 0, 9, 8, 15, 10}
mezcla = zip(numeros_tupla, letras, identificadores, conjunto)
mezcla_tupla = zip(numeros_tupla, letras)


# print(type(mezcla))
# print(type(mezcla_tupla))

# print(f"Ubicación en memoria de la mezcla: {mezcla}")
# Converir a lista para poder listar los elementos
mezcla = list(mezcla)
mezcla_tupla = tuple(mezcla_tupla)

print(f"\nSe crea una lista de tuplas: {mezcla}\n")
# print(f"Se crea una tupla de tuplas: {mezcla_tupla}")

# print(type(mezcla))
# print(type(mezcla_tupla))
