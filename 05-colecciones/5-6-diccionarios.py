# Diccionarios(key, value)

diccionario = {
    "IDE": "Integrated Development Environment",
    "OOP": "Object Oriented Programming",
    "DBMS": "Database Management System",
}

print(diccionario)

print("\nConociendo el largo de un diccionario")
print(len(diccionario))


print("\nAccediendo a elementos del diccionario")
print(f'\tdiccionario["IDE"]: {diccionario["IDE"]}')

print("\nOtra forma de accerder a un elemento de un diccionario")
print(f'\tdiccionario["IDE"]: {diccionario["IDE"]}')

print("\nModificando elementos")
print("\tModificando elemento 'IDE' ")
diccionario["IDE"] = "integrated development environment"
print(f'\tdiccionario["IDE"]: {diccionario["IDE"]}')
print(diccionario)

print("\nRecorrer los elementos de un diccionario")
for termino in diccionario:
    print(f"\t- {termino} ")

print("\nMostrar llave y valor con ciclo for")
for termino, valor in diccionario.items():
    print(f"\t{termino} - {valor}")

print("\nMostrar llave con ciclo for")
for termino in diccionario.keys():
    print(f"\t- {termino}")

print("\nMostrar valor con ciclo for")
for valor in diccionario.values():
    print(f"\t- {valor}")

print("\nComprobar existencia de algún elemento")
print("IDE" in diccionario)
print("ide" in diccionario)

print("\nAgregar un nuevo elemento")
diccionario["PK"] = "Primary Key"
print(diccionario)
print(
    """\n
Remover un elemento especificando llave,
con función pop()
      """
)
diccionario.pop("IDE")
print(diccionario)

print("\nLimpiar un diccionario con función .clear()")
diccionario.clear()
print(diccionario)

print(
    """
      \nEliminar la variable de diccionario 
de memoria con keyword 'del'
    """
)

del diccionario


try:
    print(diccionario)
except (NameError, AssertionError):
    print("\nEliminando de memoria el diccionario")
    print("No existe el valor solicitado\n")

print(diccionario)
