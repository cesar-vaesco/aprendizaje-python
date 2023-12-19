# Una función lambda sin funciones anónimas y son pequeñas
#  Una línea de código

# No es posible asignar una función a una variable de forma directa
# mi_funcion = def sumar(a, b): return a + b

# Con una función lambda  (anónima, sin nombre y en una línea de código)
#  No se necesita agregar paréntesis para los parámetros
#  no se necesita la palabra return, pero sí debe regresar una expresión

mi_funcion_lambda = lambda a, b: a + b
resultado = mi_funcion_lambda(4, 6)

print(f"resultado: {resultado}")
print(f"resultado: {mi_funcion_lambda(5, 7)}")

# Utilizar función lambda que no recibe argumentos
mi_funcion_lambda = lambda: "Mi función lambda sin argumentos"
resultado = mi_funcion_lambda()
print(f"Llamar función lambda sin argumentos: {mi_funcion_lambda}")
print(f"Llamar función lambda sin argumentos: {resultado}")


#  Función lambda con parámetros por default
mi_funcion_lambda = lambda a=2, b=3: a + b
resultado = mi_funcion_lambda()
print(f"Resultado argumentos por default: {resultado}")

resultado = mi_funcion_lambda(6, 12)
print(f"Resultado: {resultado}")


# Función lambda con argumentos variables utilizando *args - **kwargs
mi_funcion_lambda = lambda *args, **kwargs: len(args) + len(kwargs)
print(f"Resultado argumentos variables: {mi_funcion_lambda(2,4,6, a=5, b=6 )}")


# Funciones lambda con argumentos, argumentos variables y variables por default
mi_funcion_lambda = (
    lambda a, b, c=3, *args, **kwargs: a + b + c + len(args) + len(kwargs)
)

print(
    f"Resultado argumentos variables: {mi_funcion_lambda(1, 2, 4, 5, 6,7, e=5, f= 6)}"
)
