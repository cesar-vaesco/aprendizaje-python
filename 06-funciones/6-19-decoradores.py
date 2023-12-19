# Decoradores
# Es una función que recibe a su vez una función y regresa otra
# Se utiliza para extender funcionalidad

# 1.- Función decorador (a)

# 2.- Función a decorar (b)

# 3.- Función decorada (c)


def funcion_decorador_a(funcion_a_decorar_b):
    def funcion_decorada_c():
        print("\nAntes de ejecutar la función ")
        funcion_a_decorar_b()
        print("Después de ejecutar la función")

    return funcion_decorada_c


def medir_tiempo_ejecucion_funcion(function):
    def wrapper(*args, **kwargs):
        import time

        inicio = time.time()
        resultado = function(*args, **kwargs)
        total = time.time() - inicio
        print(f"Tiempo de ejecución de la función: {total} segundos")
        return resultado

    return wrapper


@medir_tiempo_ejecucion_funcion
@funcion_decorador_a
def mostrar_mensaje():
    print("Hola desde función mostrar mensaje")


@medir_tiempo_ejecucion_funcion
@funcion_decorador_a
def mensaje_despedida():
    print("Adios desde función despedida")


mostrar_mensaje()
mensaje_despedida()
