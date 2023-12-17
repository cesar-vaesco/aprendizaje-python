# print(dir(__builtins__))
# help(zip)

numeros = [1, 2, 3]
numeros_tupla = (1, 2, 3)
letras = ["a", "b", "c"]
mezcla = zip(numeros, letras)
mezcla_tupla = zip(numeros_tupla, letras)

print(type(mezcla))

print(f"Ubicación en memoria de la mezcla: {mezcla}")
# Converir a lista para poder listar los elementos
mezcla = list(mezcla)
mezcla_tupla = tuple(mezcla_tupla)

print(f"Se crea una lista de tuplas: {mezcla}")
print(f"Se crea una tupla de tuplas: {mezcla_tupla}")
