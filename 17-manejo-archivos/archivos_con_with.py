from manejo_archivos import ManejoArchivos


# with open("17-manejo-archivos/prueba.txt", "r", encoding="utf8") as archivo:
with ManejoArchivos("17-manejo-archivos/prueba.txt") as archivo:
    print(archivo.read())
