frutas = ("Naranja", "Platano", "Guayaba", "Uva")


print(frutas)

print("Conocer el largo de una tupla con funcion len(tupla): ", len(frutas))

print("\t\nElementos de la tupla por indice (frutas[0]): ", frutas[0])
print("\t\nElementos de la tupla por indice inverso (frutas[-1]): ", frutas[-1])

print(
    "\t\nAcceder a un rango (frutas[1:3]):",
    frutas[1:3],
    "   <-- No se incluye el último índice de la tupla",
)

print("\n\tRecorrer elementos de la tupla con ciclo for\t")

print("\n")
for fruta in frutas:
    print("- ", fruta, end=" \n")

print("\nNo se puede cambiar el valor de un elemento de una tupla")

print("\nSe puede cambiar de tipo tupla a tipo lista")

print("\nFrutas es de tipo: ", type(frutas))

print("\nCastear y asignar a una nueva variable la tupla")
frutasList = list(frutas)
print("Elementos de la lista casteada de una tupla")
print(frutasList)
print("Tipo de dato de frutasList:", type(frutasList))
print("\n Castear y convertir frutasList a una tupla")

frutasTupla = tuple(frutasList)

print(frutasTupla)
print("Frutas tupla es de tipo: ", type(frutasTupla))
