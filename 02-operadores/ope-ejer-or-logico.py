'''

'''

vacaciones = int(input("Vacaciones -  1 = si  / 0 = no "))
diasDescanso = int(input("Dias de descanso -  1 = si  / 0 = no  "))

if vacaciones == 1:
    vacaciones = True
else:
<<<<<<< HEAD:02-operadores/ope-ejer-or-logico.py
    vacaciones = False
=======
    vacaciones = False
>>>>>>> 3c8781e968d113abea69aa0b2e3a091556772e45:operadores/ope-ejer-or-logico.py

if diasDescanso == 1:
    diasDescanso = True
else:
    diasDescanso = False 


print(f'Vacaciones?: {vacaciones}')
<<<<<<< HEAD:02-operadores/ope-ejer-or-logico.py
print(f'Dias de descanso?: {diasDescanso}')

if not vacaciones and diasDescanso:
    print("No hay posibilidades de que pueda asistir al juego")
elif vacaciones or diasDescanso:
    print("Hay posibilidades de que pueda asistir al juego")
else:
    print("Puedo asistir al juego")
=======
print(f'Vacaciones?: {diasDescanso}')

if vacaciones == True and diasDescanso == True:
    print("Puedo asistir al juego")
elif vacaciones == True or diasDescanso == True:
    print("Hay posibilidades de que pueda asistir al juego")
else:
    print("No hay posibilidades de que pueda asistir al juego")
>>>>>>> 3c8781e968d113abea69aa0b2e3a091556772e45:operadores/ope-ejer-or-logico.py
