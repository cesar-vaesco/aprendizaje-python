# Un closure es una función que define a otra y además la puede regresar
# La función anidada puede acceder a las variables locales definidas en
#  la función principal


# función principal
def operacion(a, b):
    # Definimos una función interna o anidada
    def sumar():
        return a + b

    # Retornar la función
    return sumar


mi_funcion_closure = operacion(5, 2)
print(f"Resultado de la función closure: {mi_funcion_closure()}")


# Llamar la función regresada al vuelo (en tiempo de interpretación)
print(f"Resultado de la función closure al vuelo: {operacion(5,6)()}")

"""
def operacion(a, b):
    # Definimos una función interna o anidada
    def sumar():
        return a + b

    # Retornar la función
    return sumar

"""


# Función principal
def operacion_closure_lambda(a, b):
    # Función lambda interna o anidada
    return lambda: a + b


resultado = operacion_closure_lambda(5, 6)
print(f"Resultado funcion closure_lambda: {resultado()}")
print(f"Resultado funcion closure_lambda al vuelo: {operacion_closure_lambda(5,9)()}")
