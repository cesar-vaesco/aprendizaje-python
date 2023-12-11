import urllib
from urllib.request import urlopen


peticion = urllib.request.Request(
    "http://globalmentoring.com.mx/recursos/GlobalMentoring.txt",
    data=None,
    headers={
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/35.0.1916.47 Safari/537.36"
    },
)

with urlopen(peticion) as mensaje:
    contenido = mensaje.read().decode("utf-8")


# Contar ocurrencias de una cadena dentro de otra
#
print("No. de ocurrencias: ", contenido.count("Universidad"))

# Todo el contenido a mayusculas
print(contenido.upper())
print(contenido)

print(contenido.lower())

# Buscamos la cadena python en el contenido
print("Existe python?:", "python".lower() in contenido.lower())
print("Existe python?:", "python".upper() in contenido.upper())

# Startswith
print("Inicia con: ", contenido.startswith("En GlobalMentoring.com.mx"))


# Endswith
print("Termina con: ", contenido.endswith("GlobalMentoring.com.mx"))

mensaje = "Hola mundo"

print(mensaje.islower())
print(mensaje.lower().islower())

print(mensaje.isupper())
print(mensaje.upper().isupper())
