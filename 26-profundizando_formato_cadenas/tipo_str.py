"""
# Dar formato a un string
nombre = "Cesario"
edad = 28

# Se sustituyen valorers de izquierda a derecha
# mensaje_con_formato = "Mi nombre es %s y tengo %d años" % (nombre, edad)
# print(mensaje_con_formato)


# Se pasa una tupla con los valores a sustituir valores los cuales nunca se declara su nombre
# pero se usan por inferencia

# persona = ("Karla", "Goméz", 5000.00)
# mensaje_con_formato = "Hola %s %s. Tu sueldo es de %.5f" % persona
# print(mensaje_con_formato)

# # Se pasa la tupla hasta la delcaración de la variable
# mensaje_con_formato = "Hola %s %s. Tu sueldo es de %.5f"
# print(mensaje_con_formato % persona)
"""

nombre = "Cesario"
edad = 28
sueldo = 55.0450
# {} ---> placeholder
mensaje = "Nombre {} Edad {} Sueldo {:.2f}".format(nombre, edad, sueldo)
print(mensaje)

mensaje = "Nombre {0} Edad {1} sueldo {2:.2f}".format(nombre, edad, sueldo)
print(mensaje)

# Se puede modificar el índice, se toma el valor posicional de los valores en la función format
mensaje = "Sueldo {2} Edad {1} Nombre {0}".format(nombre, edad, sueldo)
print(mensaje)

# Se le da un alias a un parametro
mensaje = "Nombre {n} Edad {e} Sueldo {s:.2f}".format(n=nombre, e=edad, s=sueldo)
print(mensaje)

mensaje = "Nombre {nombre} Edad {edad} Sueldo {sueldo:.2f}".format(nombre=nombre, edad=edad, sueldo=sueldo)
print(mensaje)

# Se hace uso de un diccionario para poder pasar valores a la cadena de strings
diccionario = {"nombre": "Martin", "edad": 28, "sueldo": 55.0450}
mensaje = "Nombre {persona[nombre]} Edad {persona[edad]} Sueldo {persona[sueldo]}".format(persona=diccionario)
print( mensaje )

