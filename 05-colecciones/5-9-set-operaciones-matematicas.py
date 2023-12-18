print("Operaciones de conjuntos utilizando SET´s\n")
print(" Unión conmutativa ".center(60, "*"))
print("\n\nPersonas con distintas caracteristicas")

pelo_negro = {"Juan", "Karla", "Pedro", "María"}
pelo_rubio = {"Lorenzo", "Laura", "Marco"}
ojos_cafe = {"Karla", "Laura"}
menores_30 = {"Juan", "Karla", "María"}

print("Todos con ojos_cafe y pelo rubio (Union) - (No se repiten elementos)")
print(ojos_cafe.union(pelo_rubio))
print(
    "Orden inverso - Todos con ojos_cafe y pelo rubio (Union) - (No se repiten elementos)"
)
print(pelo_rubio.union(ojos_cafe))
