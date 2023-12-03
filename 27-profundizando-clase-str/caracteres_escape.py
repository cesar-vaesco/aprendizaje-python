resultado = "Hola ' mundo"

print(f"Resultado : {resultado}")

# \b --> backespace: elimina el último caracter
resultado = "Se va a eliminar el punto.\b\b\b"

print(resultado)

# Directorio
resultado = "c:\\directorio\\escritorio"
print(resultado)

"""
una cadena sin formato es un tipo especial de cadena que 
le permite incluir barras invertidas (\) 
sin interpretarlas como secuencias de escape
"""
resultado = r"Este es un \n salto de línea"
print(f"Resultado : {resultado}")

resultado = "Este es un \n salto de línea"
print(f"Resultado : {resultado}")
