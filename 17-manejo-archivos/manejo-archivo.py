# archivo = None
try:
    archivo = open("17-manejo-archivos/prueba.txt", "w", encoding="utf8")
    archivo.write("Agregamos información al archivo")
    archivo.write("\nAdios...")
except Exception as e:
    print(e)
finally:
    print("\nFin del archivo...\n")
    archivo.close()
