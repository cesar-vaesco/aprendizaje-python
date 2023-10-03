"""
Operador and - or - not
"""

valor = int(input("Ingresa un valor    "))
valor2 = int(input("Ingresa segundo valor    "))

if valor == 0 and valor2 == 2:
    print(f"Los valores {valor} y {valor2} son 0 y 2")
else:
    print(f"Los valores no coincidieron")


if valor == 0 or valor2 == 2:
    print(f"Los valores {valor} y {valor2} pueden ser o 0 y 2")
else:
    print(f"Los valores no coincidieron")

a = False
b = True

print(f'Valor de a: {a} - Valor de b: {b}')
print(f'Revirtiendo el valor de a con operador not')

a = not a

print(f'Valor de a: {a} - Valor de b: {b}')
