'''
Comparar si el valor se encuentra dentro de un rango
'''

valor = int(input("Ingresa un valor númerico   "))
valorMinimo = 0
valorMaximo = 5

if valor >= valorMinimo and valor <= valorMaximo:
    print(f'{valor} se encuentra entre el rango de 0 a 5')
elif valor < 0:
    print(f'{valor} en rango negativo')    
else:
    print(f'{valor} no se encuentra entre el rango de 0 a 5')    