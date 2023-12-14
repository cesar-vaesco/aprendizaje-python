nombres = ["Vero", "César", "Gloria", "Vanessa"]

print("")
print("\t", nombres)

print("")
print("\t", nombres[0])
print("\t", nombres[3])


print("Acceder a los elementos de la lista de manera inversa\n")

print("\t", nombres)
print("-", nombres[-3])
print("-", nombres[-1])

print("\tRecuperar valores por rango")
print(nombres[2:])
# Imprimir un rango
print(nombres[1:4])
# Sin incluir el indice 3
print(nombres[1:3])
# Ir del inicio de la lista al Índice (Sin incluirlo)
print(nombres[:3])
# Desde el Índice indicado hasta el final
print(nombres[1:])
# Cambiar el valor de un elemento de la lista
nombres[3] = "Aurelio"
print("Agregar un nuevo elemento a la lista")
nombres.append("Vanessa")
print(nombres)

print("")
for nombre in nombres:
    print("\t", nombre)
else:
    print("\nNo existen más nombres en la lista")
print("")

# Preguntar el largo de una lista
print("Elementos en la lista:", len(nombres))
print("\nAgregar un nuevo elemento a la lista")
nombres.append("Maki")
print("\nElementos en la lista:", len(nombres))
print(nombres)
# Insertar un nuevo elemento a la lista
# desde un índice definido
print("\nInsertar un nuevo elemento desde un índice definido")
nombres.insert(0, "Bronco")
print(nombres)
print("\nRemover un elemento de la lista")
nombres.remove("Bronco")
print(nombres)
print("\nRemover el último elemento de la lista con función pop()")
nombres.pop()
print(nombres)
print("\nEliminar un elemento de la lista desde un índice indicado")
del nombres[1]
print(nombres)
print(
    """
    \nEliminar todos los elementos de la lista 
      desde un índice indicado con función clear()"
    """
)
nombres.clear()
print("- Elementos de lista: ", nombres)

print("Eliminar la asignación en memoria de la lista")
# del nombres
# print(nombres)


nombres1 = ["César", "Artemia", "Susana"]
nombres2 = "Jorge María José".split(" ")

print()
print(" Suma de listas ".center(50, "*"))

print(f"Lista1: {nombres1}")
print(f"Lista2: {nombres2}\n")


print(f"Sumar listas: {nombres1 + nombres2}\n")

print(" Extender una lista con otra lista ".center(50, "*"))

nombres1.extend(nombres2)

print(f"Extender la lista uno con la lista 2: {nombres1}\n")

#  Lista de números
numeros1 = [1, 40, 3, 4, 5, 20, 7, 4]

# Obtener el primer indice del primer elemento encontrado en la lista
# help(list.index)
print(f"Lista original: {numeros1}")
print(f"Indice 4: {numeros1.index(4)}")

# Invertir los numeros de una lista
numeros1.reverse()
print(f"Lista invertida: {numeros1}")

# Ordenar los elementos de una lista ascendente
numeros1.sort()
print(f"Lista ordenada: {numeros1}")

# Ordenar los elementos de una lista de forma descendente
numeros1.sort(reverse=True)
print(f"Lista ordenada de forma descendente: {numeros1}")

# Obtener ek valor minimo y maximo de una lista
print(f"Valor minimo: {min(numeros1)}")
print(f"Valor máximo: {max(numeros1)}")

# Copiar los elementos de una lista
numeros2 = numeros1.copy()
print(f"Lista original: {numeros1}")
print(f"Lista copia: {numeros2}")

print(f"Misma referencia? {numeros1 is numeros2}")
print(f"Mismo contenido? {numeros1 == numeros2}")

# Podemos usar el constructor de la lista
print(" Podemos usar el constructor de la lista --> numeros2 = list(numeros1) ")
numeros2 = list(numeros1)
print(f"Misma referencia? {numeros1 is numeros2}")
print(f"Mismo contenido? {numeros1 == numeros2}")

print("slicing -->>> copiar elementos de una lista en por otra lista")
numeros2 = numeros1[:]
print("slicing --> numeros2 = numeros1[:]")

print(f"Misma referencia? {numeros1 is numeros2}")
print(f"Mismo contenido? {numeros1 == numeros2}")

# Multiplicacion de listas

lista_multiplicacion = 5 * [[2, 5]]

print(lista_multiplicacion)
print(f"Misma referencia: {lista_multiplicacion[0] is lista_multiplicacion[1]}")
print(f"Mismo contenido: {lista_multiplicacion[0] == lista_multiplicacion[1]}")

# Se modifica todos los elementos de la lista
lista_multiplicacion[2].append(10)
print(lista_multiplicacion)

# Matrices en python --> lista de listas
print("\n", " Matrices en python --> lista de listas ".center(100, "*"))
matriz = [[10, 20], [30, 40, 50], [60, 70, 80, 90]]
print(f"Matriz original: {matriz}")
print(
    f"Elementos de la primera lista contenida en la matriz: {matriz[0][0]} - {matriz[0][1]}"
)
print(
    f"Elementos de la segunda lista contenida en la matriz: {matriz[1][0]} - {matriz[1][1]} - {matriz[1][2]}"
)
print(
    f"Elementos de la tercera lista contenida en la matriz: {matriz[2][0]} - {matriz[2][1]} - {matriz[2][2]} - {matriz[2][3]}"
)

print(f"Renglón 0, columna 0: {matriz[0][0]}")
print(f"Renglón 1, columna 2: {matriz[1][2]}")
print(f"Renglón 2, columna 3: {matriz[2][3]}")

matriz[0][0] = 105

print(f"Modificación - Renglón 0, columna 0: {matriz[0][0]}")

print(f"Matriz original: {matriz}")

print("Agregando un nuevo elemento a la fila 0")
matriz[0].append(180)
print(f"Matriz modificada con el nuevo elemento: \n\t\t\t\t\t{matriz}")

print(" \n", "Ordenar lista de listas")

lista_listas = [[5, 8, 6, 45, 12], [56, 89, 15], [45, 12, 89, 65, 20, 35, 65]]
print(
    "Ordenamiento de la matriz segun el tipo de elementos que tengan los renglones (lista_listas.sort(key=len)) "
)
lista_listas.sort(key=len)
print(f"Ordenar lista: {lista_listas}")

#  built-in --> función parte del lenguaje de python

# help(sorted)
nombres1 = ["César", "Vane", "Gloria", "Vero", "Aurelio"]

print(f"Lista original de nombres: {nombres1}")
nombres1 = sorted(nombres1)
print(f"Ordenamiento alfabetico de la lista de forma ascendente: {nombres1}")

nombres1 = sorted(nombres1, reverse=True)
print(f"Ordenamiento alfabetico de la lista de forma descendente: {nombres1}")

print("Ordenar por la cantidad de los caractres (largo)")
nombres1 = sorted(nombres1, key=len)

print(f"Ordenar por la cantidad de los caracteres (largo): {nombres1}")

print("\n built-in revese")
# reversed se aplica directamente, en la función sorted se pasaba como parametro
nombres1 = reversed(nombres1)
print(nombres1)
print(list(nombres1))
