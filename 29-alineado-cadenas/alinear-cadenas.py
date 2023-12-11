# Centrar un string

titulo = " Sitio web de google.com.mx "

print("Caracteres de la caderna titulo: ", len(titulo))

print(titulo.center(50, "*"))

print("Caracteres de la caderna titulo: ", len(titulo.center(50, "#")))

print(titulo.center(len(titulo) + 10, "-"))
