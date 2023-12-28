# Expresión generadora - generador anónimo

multiplicacion = (valor * valor for valor in range(4))


print(f"Objeto: {multiplicacion}")
print(f"Tipo: {type(multiplicacion)}")

print("\n", " Mandar traer valores del generador ".center(60, "*"), "\n")

try:
    print(f"Valor: {next(multiplicacion)}")
    print(f"Valor: {next(multiplicacion)}")
    print(f"Valor: {next(multiplicacion)}")
    print(f"Valor: {next(multiplicacion)}")
    print(f"Valor: {next(multiplicacion)}")
except StopIteration:
    print("\t --> StopIteration <--")

print("\n", " Pasando expresión generadora a una función...  ".center(60, "*"), "\n")

suma = sum(valor * valor for valor in range(0, 4))
print(f"Resultado suma: {suma}")
print("\n", " Usando una lista...  ".center(60, "*"), "\n")


lista = ["Juan", "Pérez"]

generador = (valor for valor in lista)

print(next(generador))
print(next(generador))

print(
    "\n",
    " Crear un string a partir de un generador creado a partir de una lista...  ".center(
        80, "*"
    ),
    "\n",
)


lista = ["Karla", "Gómez", 22]
print(f"Lista a modificar: {lista}")
contador = 0


def incrementar():
    global contador
    contador += 1
    return contador


#  Primera parte es el yield del generador, la segunda es el for entre parentesís
generador = (f"{incrementar()}. {nombre}" for nombre in lista)

lista = list(generador)
print(lista)

cadena = ", ".join(lista)
print(f"Cadena modificada: {cadena}")
print(f"Tipo de dato de la variable cadena: {type(cadena)}")
