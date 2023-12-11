# Centrar un string

titulo = " Sitio web de google.com.mx "

print("Caracteres de la caderna titulo: ", len(titulo))

print(titulo.center(50, "*"))

print("Caracteres de la caderna titulo: ", len(titulo.center(50, "#")))

print(titulo.center(len(titulo) + 10, "-"))

print("alineando cadenas a la izquierda".center(100, "<"))

print(titulo.ljust(50, "-"))
print(titulo.ljust(len(titulo) + 10, "-"))

print("alineando cadenas a la derecha".center(100, ">"))

print(titulo.rjust(50, ">"))
print(titulo.rjust(len(titulo) + 10, ">"))
