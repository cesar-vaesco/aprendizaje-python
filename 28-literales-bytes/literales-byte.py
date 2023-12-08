caracteres_en_bytes = b"Hola Mundo"
print(caracteres_en_bytes)

# Se muestra el valor en bytes
mensaje = b"Universidad Python"
print(mensaje[0])
print(chr(mensaje[0]))

lista_caracteres = mensaje.split()
print(lista_caracteres)

# Converir string a bytes
string = "Programación con python"
print(f"String original: {string}")

bytes = string.encode("UTF-8")
print(f"Bytes codificado: {bytes}")

# Convertir de bytes astring
string2 = bytes.decode("UTF-8")
print(f"String decodificado: {string2}")
print(string == string2)
