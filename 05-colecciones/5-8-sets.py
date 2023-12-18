print("SET --> Colección de elementos únicos".center(60, "*"))
print("Elementos de SET deben de ser inmutables".center(60, "*"))

conjunto = {"Juan", True, 2.5}
print(conjunto)

print("SET vacio --> ")
# set vacio
conjunto = {}
print(type(conjunto))

print("SET vacio se requiere utilizar el constructor de los set --> ")
conjunto = set()
print(type(conjunto))

print("Agregar un elemento a un SET usando el método add()")
conjunto.add("Juan")
print(conjunto)
print("Un SET contiene valores únicos, no acepta dúplicados")
conjunto.add("Juan")
print(conjunto)

print("Crear un SET a partir de un iterable")
print("Lista: ")
numeros = [1, 2, 3, 4, 5]
numeros = set(numeros)
print(type(numeros))
print(numeros)

print("\nTupla: ")
numeros = (1, 2, 3, 4, 5)
print(type(numeros))
print(numeros)
numeros = set(numeros)
print(type(numeros))
print(numeros, "\n")
