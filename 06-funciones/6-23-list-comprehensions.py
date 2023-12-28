numeros = range(10)

lista_mostrar_pares = []
lista_pares = []

# Creamos una nueva lista con los valores pares
for numero in numeros:
    # Validar número par
    if numero % 2 == 0:
        print(f"{numero} es par ")
        lista_mostrar_pares.append(numero)
        # Números pares multiplicados por si mismo
        lista_pares.append(numero * numero)
    elif numero % 2 != 0:
        print(f"{numero} es impar ")

print(f"Numeros pares de la lista: {lista_mostrar_pares}")
print(f"Numeros pares múltiplicados por sí mismo: {lista_pares}")

print("\n", " Mismo ejercicio pero con list-comprehensions ".center(60, "*"))
# [expresion for var in colección if condicion]
#  If es una condición opcional

lista_pares = [numero * numero for numero in numeros if numero % 2 == 0]
print(f"Numeros pares de la lista: {lista_mostrar_pares}")
print(f"[list comprehensions] Numeros pares múltiplicados por sí mismo: {lista_pares}")

print(
    "\n",
    " Mismo ejercicio similar pero con dos condiciones pero con list-comprehensions ".center(
        60, "*"
    ),
)
print("\t Sólo se agrega el valor a la lista cuando el valor cumple ambas condiciones")

pares = [numero for numero in range(50) if numero % 2 == 0 if numero % 6 == 0]
print(f"Número divisible entre 2 y entre 6 de la lista: {pares}")

print("\ncon uso de if-else")

lista_pares = []
lista_impares = []

for numero in range(10):
    if numero % 2 == 0:
        lista_pares.append(numero)
    else:
        lista_impares.append(numero)

print(f"Lista pares: {lista_pares}")
print(f"Lista impares: {lista_impares}")


print(
    "\n[list-comprehensions] Sólo se agrega el valor a la lista cuando el valor cumple ambas condiciones"
)
lista_pares = []
lista_impares = []

[
    lista_pares.append(numero) if numero % 2 == 0 else lista_impares.append(numero)
    for numero in range(10)
]

print(f"[list-comprehensions] Lista pares: {lista_pares}")
print(f"[list-comprehensions] Lista impares: {lista_impares}")
