# Pasando valores por default a la función
# -> sólo índica una pista del tipo esperado de retorno de la función
def restar(a=0, b=0) -> int:
    return a - b


def sumar(a=0, b=0):
    return a + b


resultado = sumar(5, 3)
resultado_res = restar(5, 3)

print(f"El resultado de la suma con valores por default es: {sumar()}")
print(f"Resultado de la suma: {resultado}")
print(f"Resultado de la resta: {resultado_res}")
