# Funcion conr *args para multiplicar


def multiplicar(*args):
    resultado = 1
    for valor in args:
        resultado *= valor
    return resultado


print(f"Resultado multiplicación: {multiplicar(5,4,2)}")
