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
del nombres
print(nombres)