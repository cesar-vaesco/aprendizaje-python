#
try:
    # archivo = open("c:\\Users\\cesar\\Desktop\\python_curso\\17-manejo-archivos\\prueba.txt", "r", encoding="utf8")
    archivo = open("17-manejo-archivos/prueba.txt", "r", encoding="utf8")
    # Recuperando caracteres de un archivo --> cantidad
    # print(archivo.read(10))
    # Leer línea completa
    # print(archivo.readline())
    # print(archivo.readline())
    # print(archivo.read())

    # for linea in archivo:
    #     print(linea)

    # Leer lineas
    # print(archivo.readlines())

    # Acceder a una linea de la lista
    # print(archivo.readlines()[2])

    # Abrimos un nuevo archivo
    # a - anexar información
    archivo2 = open("17-manejo-archivos/copia.txt", "w", encoding="utf8")
    archivo2.write(archivo.read())

except Exception as e:
    print(e)

finally:
    archivo.close()
    archivo2.close()
    print("Cerrando archivo")
