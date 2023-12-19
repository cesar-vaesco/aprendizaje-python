# Las funciones en python son ciudadanas de primera clase
# First class citizens


# Definimos la función


def sumar(a, b):
    return a + b


# Asignar función a una variable( no se usan parentesis)
mi_funcion = sumar

# Varificar el tipo de la variable
print(type(mi_funcion))

# Llamamos la función a través de la
resultado = mi_funcion(8, 5)
print(f"Resultado: {resultado}")
