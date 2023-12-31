print("Operaciones de conjuntos utilizando SET´s\n")
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


print("Intercepción  (Unión conmutativa) ".center(60, "*"))

print(
    "\n Intercepción -> recupera sólo los elementos que se encuentran en ambos conjuntos".center(
        60, "*"
    )
)

print("\tRecuperar las personas de ojos café y pelo rubio: ")
print(ojos_cafe.intersection(pelo_rubio))
print(
    f"\tConmutativa --> se invierte el orden de la generación de la intercepción : {pelo_rubio.intersection(ojos_cafe)}"
)

print("Diference--> elementos que no se repiten - No es conmutativa ".center(60, "*"))
print("\t** Personas que se encuentran en el primer SET pero no en el segundo **")
print(
    f"Personas que tienen pelo negro sin ojos café: {pelo_negro.difference(ojos_cafe)}"
)

print(
    "Diferencia símetrica--> regresa las coincidencias entre conjuntos".center(60, "*")
)
print("Personas con pelo negro u ojos cafés, pero no ambos (conmutativa): ")
print(f"set pelo_negro: {pelo_negro}")
print(f"set ojos_cafe: {ojos_cafe}")
print(
    "\tpelo_negro.symmetric_difference(ojos_cafe): ",
    pelo_negro.symmetric_difference(ojos_cafe),
)


print("\nUn set esta contenido en otro -- SUBSET")
print(f"Primer set: {menores_30}")
print(f"Segundo set: {pelo_negro}")
print(
    "\t\nRevisamos si los elementos del primer set están contenidos en el segundo set: "
)
print(menores_30.issubset(pelo_negro))

print("\n", " SUPERSET: un set contiene a otro set ".center(50, "*"))
print(
    "Revisar si los elementos del primer set estan contenidos dentro del segundo set: "
)
print("Las personas menores de 30 es un super set de las personas de pelo negro")
print(f"Menores de 30: {menores_30}")
print(f"Pelo negro: {pelo_negro}")
print(f"Superset: ? {menores_30.issuperset(pelo_negro)}")
print("Las personas de pelo negro son un super set de las personas menores de 30? ")
print(f"Superset: ? {pelo_negro.issuperset(menores_30)}")
print(
    "\n",
    "DISTJOIN --> las personas de pelo negro no tienen pelo rubio ".center(60, "*"),
)
print(pelo_negro.isdisjoint(pelo_rubio))
