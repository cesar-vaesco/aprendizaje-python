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
