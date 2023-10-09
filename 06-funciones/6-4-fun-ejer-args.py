"""
Función que suma valores recibidos de tipo numerico
utilia argumentos variables como parametro de función
y regresa como resultado la suma de todos los valores pasados como 
argumentos
"""


def sumar_valores(*args):
    resultado = 0
    for valor in args:
        resultado += valor
    print(resultado)


def restar_valores(*args):
    resultado = 0
    for valor in args:
        resultado -= valor
    return resultado


resultado_resta = restar_valores(5, 3, 1)

sumar_valores(10, 5, 12)
print(f"Resultado resta: {resultado_resta}")
