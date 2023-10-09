factorial = int(input("Ingrese número para obtener factorial:   "))


def buscar_factorial(numero):
    if numero == 1:
        return 1
    else:
        return numero * buscar_factorial(numero - 1)


print(f"El factorial de {factorial} es: {buscar_factorial(factorial)}")
