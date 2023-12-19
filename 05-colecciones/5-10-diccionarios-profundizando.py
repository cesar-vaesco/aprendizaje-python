print("Los diccionarios guardan un orden (los set no guardan orden) ".center(60, "*"))


diccionario = {"Nombre": "Juan", "Apellido": "Peréz", "Edad": 28}
print(diccionario)
print("Los diccionarios son mutables, pero las llaves deben ser inmutables")
print("Diccionario : {'Llave': 'Valor'}")
diccionario = {(1, 2): "Valor1"}
print(diccionario)

diccionario = {"Nombre": "Juan", "Apellido": "Peréz", "Edad": 28}
print(
    "Se agrega una llave con su valor, si no se encuentra dentro del  - Crea o remplaza"
)
diccionario["Departamento"] = "Sistemas"
print(diccionario)
print(
    "Los diccionarios no acepta valor duplicados en las llaves de un diccionario, si ya existe se rempalza"
)

diccionario["Nombre"] = "Joan Charly"
print(diccionario)

print("Recuperando un valor indicando una llave".center(60, "*"))

print("Nombre: ", diccionario["Nombre"])
# Sí no encuentra la llave lanza una excepción

print("Método get recupera una llave y si no existe NO lanza excepcion")
print(diccionario.get("nombre", "No se encontro la llave"))
print("No se modifica el diccionario", diccionario)

print(
    "Método setdefault si modifica el diccionario en caso de que no es encuentre la llave ademas se agrega un valor por default"
)

nombre = diccionario.setdefault("Nombre", "Valor default")
print(nombre)
print(diccionario)
direccion = diccionario.setdefault("Direccion", "Por definir")
print(diccionario)

print("\npprint para imprimir un diccionario\n")
from pprint import pprint as pp

diccionario["Direccion"] = "Ecatepec, México"

print("\nOrden alfabetica: ")
pp(diccionario)
print("\nImpresión como se fueron agregando los elementos: ")
pp(diccionario, sort_dicts=False)
