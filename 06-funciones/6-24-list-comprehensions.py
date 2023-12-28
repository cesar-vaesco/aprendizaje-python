#  Lista de listas
lista_listas = [[1, 2, 3], [4, 5, 6], [7, 8, 9, 10]]

# Convertir la lista de listas en una sola lista
lista_simple = [sublista for sublista in lista_listas]
print(f"Lista simple: {lista_simple}")

lista_simple = [valor for sublista in lista_listas for valor in sublista]
print(f"Lista simple: {lista_simple}")


lista_numeros_pares = []
for sublista in lista_listas:
    for valor in sublista:
        if valor % 2 == 0:
            lista_numeros_pares.append(valor)

print(f"Numeros pares de la lista: {lista_numeros_pares}")

print("\n[List Comprehensions] obtención de números pares")

lista_numeros_pares = [
    valor for sublista in lista_listas for valor in sublista if valor % 2 == 0
]
print(f"[List comprehensions] Numeros pares de la lista: {lista_numeros_pares}")
