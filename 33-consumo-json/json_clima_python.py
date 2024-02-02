import json
import urllib.request


peticion = urllib.request.Request(
    "http://globalmentoring.com.mx/api/clima.json",
    data=None,
    headers={
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/35.0.1916.47 Safari/537.36"
    },
)
respuesta = urllib.request.urlopen(peticion)
# print(respuesta)

cuerpo_respuesta = respuesta.read()
# print(cuerpo_respuesta)

# Procesamos la respuesta
json_respuesta = json.loads(cuerpo_respuesta.decode("utf-8"))
# print(json_respuesta)

# Acceder a la descripción del clima

# descripcion_clima = json_respuesta.get("clima")[0]
# descripcion_clima1 = json_respuesta.get("clima")[0]["descripcion"]
# print(f"Descripción del clima 1: {descripcion_clima1}")
descripcion_clima = json_respuesta.get("clima")[0].get("descripcion")
des_clima = json_respuesta["clima"][0]["descripcion"]
print(f"Descripción del clima: {descripcion_clima}")
print(f"Descripción del clima: {des_clima}")

# Mostrar la temperatura miníma y máxima
tem_min = json_respuesta.get("principal").get("temp_min")
temmin = json_respuesta["principal"]["temp_min"]
print(f"Temperatura mínima: {tem_min} C")
print(f"Temperatura mínima: {temmin} C")

tem_max = json_respuesta.get("principal").get("temp_max")
temmax = json_respuesta["principal"]["temp_max"]
print(f"Temperatura máxima: {tem_max} C")
print(f"Temperatura máxima: {temmax} C")
