# Funciones anidadas


def calculadora(a, b, operacion="sumar"):
    # 1.- Definimos la función anidada
    def sumar(a, b):
        return a + b

    def restar(a, b):
        return a - b

    def multiplicar(a, b):
        return a * b

    # 2.-  Llamada a la función anidada
    if operacion == "sumar":
        print(f"Resultado suma: {sumar(a, b)}")
    elif operacion == "restar":
        print(f"Resultado restar: {restar(a, b)}")
    elif operacion == "multiplicar":
        print(f"Resultado multiplicar: {multiplicar(a, b)}")


calculadora(6, 5)
calculadora(6, 5, "restar")
calculadora(5, 6, "multiplicar")
