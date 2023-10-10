
# Sintaxis para importar un módulo
# from "Nombre_Archivo" import "Clase"
# Si se quiere importar todas las clases que se importan 
# from "Nombre_Archivo" import *
from Persona import Persona


print(" Creación objetos ".center(30, "*"))

persona1 = Persona("Víctor","Mejía", 16)
print(persona1.mostrar_detalle())

print(" Eliminación de objetos ".center(30, "*"))

del persona1
# print(__name__)