# archivo = None
try:
    archivo = open("prueba.txt", "w", encoding="utf8")
    archivo.write("Agregamos información al archivo")
    archivo.write("\nAdios...")
except Exception as e:
    print(e)
finally:
    print("Fín del archivo...")
    archivo.close()
