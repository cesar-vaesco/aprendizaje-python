import math

from mi_clase import MiClase

# Concatenación automatica en python
# variable = "Adios"
# mensaje = "Hola"  " Mundo " +  variable
# mensaje += " Universidad" " Python"

# print(mensaje)

# help(math)

# help(str)


"""
Comentarios varías líneas
"""

# help(MiClase)
# print(MiClase.__doc__)
# print(MiClase.__init__.__doc__)
# print(MiClase.mi_metodo.__doc__)
# print(MiClase.mi_metodo)
# print(type(MiClase.mi_metodo))

help(str.capitalize)

mensaje1 = "hola mundo"
# No muta el valor de la variable mensaje1
mensaje2 = mensaje1.capitalize()

print(f"mensaje1: {mensaje1}, id: {hex(id(mensaje1))}")
print(f"mensaje2: {mensaje2}, id: {hex(id(mensaje2))}")

# se modifica la variable
mensaje1 = "adios"
print(f"mensaje1: {mensaje1}, id: {hex(id(mensaje1))}")


