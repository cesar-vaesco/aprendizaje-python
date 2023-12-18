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

print("\n Agregar más elementos a un SET o incluso otro SET al set ya declarado")
print(f"Conjunto: {conjunto}")
conjunto2 = {100, 200, 300, 300}
conjunto.update(conjunto2)
print(f"Conjunto2: {conjunto2}")
print(f"Conjunto actualizado con conjunto 2: {conjunto}")
conjunto.update([20, 30, 40, 40])
print(f"Conjunto actualizado con nuevos elementos: {conjunto}")

print("\nCopia de un SET (copia poco profunda, solo copia las referencias) ")
conjunto_copia = conjunto.copy()
print(f"Conjunto_copia: {conjunto_copia}")
print("\tVerificar igualdad de conjuntos: ")
print(f"Es igual en contenido? {conjunto ==  conjunto_copia}")
print(f"Es la misma referencia? {conjunto is  conjunto_copia}")
print(f"Id conjunto: {id(conjunto)}")
print(f"Id conjunto_copia: {id(conjunto_copia)}")
