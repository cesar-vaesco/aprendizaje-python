# Set

planetas = {"Marte", "Jupiter", "Venus"}

# Conocwer el largo de los elementos del set

print(type(planetas))
print(planetas)
print(len(planetas))

# Revisar si un elemento esta presente en un set

print("Martes" in planetas)
print("Marte" in planetas)

# Agregando un nuevo elemento en un set
planetas.add("Tierra")
print(planetas)

# No se pueden duplicar elementos
planetas.add("Marte")
print(planetas)

# Eliminar un elemento posiblemente generando un error
planetas.remove("Venus")
print(planetas)

# la función discar no genera un
# error al eliminar un elemento

planetas.discard("Venus")
print(planetas)
planetas.discard("Marte")
print(planetas)

# Limpiar un set
planetas.clear()
print(f"Limpiado el contenido del set: {planetas}")

# Eliminar set por completpo
del planetas


try:
    print(planetas)
except (NameError, AssertionError):
    print("\nEliminando de memoria el set")
    print("No existe el valor solicitado")
