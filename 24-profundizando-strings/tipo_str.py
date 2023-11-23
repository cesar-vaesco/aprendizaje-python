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

# help(str.capitalize)

# mensaje1 = "hola mundo"
# # No muta el valor de la variable mensaje1
# mensaje2 = mensaje1.capitalize()

# print(f"mensaje1: {mensaje1}, id: {hex(id(mensaje1))}")
# print(f"mensaje2: {mensaje2}, id: {hex(id(mensaje2))}")

# # se modifica la variable
# mensaje1 = "adios"
# print(f"mensaje1: {mensaje1}, id: {hex(id(mensaje1))}")


# help(str.join)

# tupla_str = ("Hola", "Mundo", "universidad", "Phyton")
# mensaje = " ".join(tupla_str)
# print(mensaje)

# lista_curso = ["Java", "Python", "Angular", "Spring"]
# mensaje = ", ".join(lista_curso)
# print(mensaje)

# cadena = "HolaMundo"
# mensaje = ".".join(cadena)
# print(mensaje)


# diccionario = {"nombre": "César", "apellido": "Varela", "Edad": "43"}
# llaves = "-".join(diccionario.keys())
# valores = " ".join(diccionario.values())
# print(f"Llaves: {llaves}")
# print(f"Valores: {valores}")
# print(type(llaves))
# print(type(valores))

# help(str.split)

cursos = "Java Python JavaScript Angular Spring Excel"
lista_cursos = cursos.split()
print(lista_cursos)

print(type(lista_cursos))

cursor_separados_coma = "Java, Python, JavaScript, Angular, Spring, Excel"
lista_cursos = cursor_separados_coma.split(", ")
print(lista_cursos)
print(len(lista_cursos))


lista_cursos = cursor_separados_coma.split(", ", maxsplit=3)
print(lista_cursos)
print(len(lista_cursos))
