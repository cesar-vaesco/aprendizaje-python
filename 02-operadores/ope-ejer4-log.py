print("\tProporcione los siguientes datos del libro:  ")

libro = input("Proporcione el nombre: ")
idLibro = input("Proporcione el ID: ")
precio = float(input("Proporcione el precio : "))
estadoEnvio = input("Indique sí el envío es gratutito (True/False)")


if estadoEnvio == "True":
    estadoEnvio = True
elif estadoEnvio == "False":
    estadoEnvio = False



print(f'''
      \tDatos del libro:\n 
      Libro: {libro} 
      Id: {idLibro}
      Precio: {precio} 
      Envio gratuito: {estadoEnvio} 
    ''')
