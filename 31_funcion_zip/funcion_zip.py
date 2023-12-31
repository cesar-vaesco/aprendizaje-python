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
# mezcla_tupla = tuple(mezcla_tupla)

print(f"\nSe crea una lista de tuplas: {mezcla}\n")
# print(f"Se crea una tupla de tuplas: {mezcla_tupla}")

# print(type(mezcla))
# print(type(mezcla_tupla))

print("\nIterar en paralelo")

for numero, letra, identificador, aleatorio in zip(
    numeros, letras, identificadores, conjunto
):
    print(
        f"""
- Número: {numero} 
- Letra: {letra} 
- Identificador: {identificador} 
- Aleatorio: {aleatorio}"""
    )


nueva_lista = []

for numero, letra, identificador, aleatorio in zip(
    numeros, letras, identificadores, conjunto
):
    nueva_lista.append(f"{identificador} - {numero} - {letra} - {aleatorio}")

print("\nCrando una nueva lista mezclando elementos de varios iterables:\n")
print("\t", nueva_lista)


# unzip
mezcla = [(1, "a"), (2, "b"), (3, "c")]
numeros, letras = zip(*mezcla)

print("\nSeparación de iterables - unzip: ")
print(f"\nNúmeros: {numeros} \nLetras: {letras}")


print("\nOrdenamiento utilizando la función zip")

letras = ["c", "d", "a", "e", "b"]
numeros = [3, 2, 1, 4, 0]

mezcla = zip(letras, numeros)

print(tuple(mezcla))

mezcla = zip(numeros, letras)

print(
    "\nOrdenamiento segun el primer iterable que se pase por parametro a la función zip"
)
print(sorted(zip(letras, numeros)))
print(sorted(zip(numeros, letras)))


print("\nCrear un diccionario a partir de dos iterables\n")

llaves = ["nombre", "apellido", "edad"]
valores = ["Juan", "Peréz", 18]
diccionario = dict(zip(llaves, valores))
print(diccionario)

print("\nActualiar un elemento de un diccionario\n")
llave = ["edad"]
nueva_edad = [28]
diccionario.update(zip(llave, nueva_edad))
print(diccionario)
