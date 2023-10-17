
# archivo = None
try:
    archivo = open("prueba.txt", "w")
    archivo.write("Agregamos información al archivo")
    archivo.write("\nAdios...")
except Exception as e:
    print(e)
finally:
    print("Cerrando archivo...")
    archivo.close()
