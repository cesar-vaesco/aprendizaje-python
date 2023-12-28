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
print(f"Resultado: {suma}")
print(f"Resultado: {suma}")
print(f"Resultado: {suma}")
print(f"Resultado: {suma}")
