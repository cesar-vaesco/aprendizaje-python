# bool contiene los valores los valores de True o False
#  Tipos númericos, False = 0 y True para los demas valores

valor = 0
valor = 0.0
resultado = bool(valor)
print(f"Valor: {valor}, resultado: {resultado}")


valor = 15
resultado = bool(valor)
print(f"Valor: {valor}, resultado: {resultado}")

# Tipo str, Falso para cadena vacía y para cualquie otro valor verdadero
valor = ""
resultado = bool(valor)
print(f"Valor: {valor}, resultado: {resultado}")

valor = "Hola"
resultado = bool(valor)
print(f"Valor: {valor}, resultado: {resultado}")


# Tipo colecciones, False colecciones vacías - Verdadero para las colecciones con algún valor

valor = []
resultado = bool(valor)
print(f"Valor: {valor}, resultado: {resultado}")

valor = {"Hola", "adios"}
resultado = bool(valor)
print(f"Valor: {valor}, resultado: {resultado}")


valor = ()
resultado = bool(valor)
print(f"Valor: {valor}, resultado: {resultado}")

valor = ("Hola", "adios")
resultado = bool(valor)
print(f"Valor: {valor}, resultado: {resultado}")


valor = {}
resultado = bool(valor)
print(f"Valor: {valor}, resultado: {resultado}")

valor = {"nombre":"César", "apellido": "Escobar"}
resultado = bool(valor)
print(f"Valor: {valor}, resultado: {resultado}")