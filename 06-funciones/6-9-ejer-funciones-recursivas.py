"""
Imprimir números de 5 a 1 de manera descendente usando recursividad
- puede ser cualquier valor positivo
- si pasa valores negativos no pasa nada 
"""


numero_descendente = int(input("Ingrese un número: "))


def imprimir_numero_recursivo(numero):
    if numero >= 1:
        print(numero)
        imprimir_numero_recursivo(numero - 1)

    elif numero == 0:
        return
    elif numero <= 0:
        print("Valor incorrecto... ")


def decremento(numero):
    if numero < 1:
        return "Ingrese sólo números positivos..."
    elif numero == 1:
        return 1
    else:
        return f"{numero} {decremento(numero - 1)}"


imprimir_numero_recursivo(numero_descendente)
print(decremento(numero_descendente))
