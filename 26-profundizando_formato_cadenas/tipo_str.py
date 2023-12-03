# Dar formato a un string
nombre = "Cesario"
edad = 28

# Se sustituyen valorers de izquierda a derecha
mensaje_con_formato = "Mi nombre es %s y tengo %d años" % (nombre, edad)
print(mensaje_con_formato)

""" 
Se pasa una tupla con los valores a sustituir valores los cuales nunca se declara su nombre 
pero se usan por inferencia  
"""
persona = ("Karla", "Goméz", 5000.00)
mensaje_con_formato = "Hola %s %s. Tu sueldo es de %.5f" % persona
print(mensaje_con_formato)

# Se pasa la tupla hasta la delcaración de la variable
mensaje_con_formato = "Hola %s %s. Tu sueldo es de %.5f"
print(mensaje_con_formato % persona)
