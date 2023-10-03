operandoA = float(input("Ingresa primer operando...  "))
operandoB = float(input("Ingresa segundo operando... "))

suma = operandoA + operandoB
resta = operandoA - operandoB
multiplicacion = operandoA * operandoB
division = operandoA / operandoB
division_entera = operandoA // operandoB
modulo = operandoA % operandoB
exponente = operandoA**operandoB

# print("Resultado suma:", suma)
print(f"Resultado suma: {suma}")
print(f"Resultado resta: {resta}")
print(f"Resultado multiplicacion: {multiplicacion}")
print(f"Resultado división: {division} y el residuo es {modulo}")
print(f"Resultado división resultado entera: {division_entera} y el residuo es {modulo}")
print(f"Resultado de exponente: {exponente}")
