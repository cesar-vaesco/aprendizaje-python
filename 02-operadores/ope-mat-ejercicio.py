# Se solicita calcular el área y el perímetro de un rectángulo
# Se requiere crear las siguientes variables: 
# alta(int)
# ancho(int)

# Usuario proporciona los valores

print("\tCalcular el área y el perímetro de un Rectangulo")

alto = int(input("Ingrese altura...   "))
ancho = int(input("Ingrese ancho...   "))

perimetro  = (alto + ancho) * 2
area = alto * ancho

print(f'Área: {area}')
print(f'Perímetro: {perimetro}')