#
try:
    # archivo = open("c:\\Users\\cesar\\Desktop\\python_curso\\17-manejo-archivos\\prueba.txt", "r", encoding="utf8")
    archivo = open("17-manejo-archivos/prueba.txt", "r", encoding="utf8")
    # Recuperando caracteres de un archivo --> cantidad
    # print(archivo.read(10))
    # Leer línea completa
    print(archivo.readline())
    print(archivo.readline())
    # print(archivo.read())

except Exception as e:
    print(e)

finally:
    archivo.close()
    print("Cerrando archivo")
