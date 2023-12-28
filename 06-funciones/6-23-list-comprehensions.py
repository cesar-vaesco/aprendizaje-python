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
