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
