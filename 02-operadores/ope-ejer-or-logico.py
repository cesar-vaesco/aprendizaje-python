'''

'''

vacaciones = int(input("Vacaciones -  1 = si  / 0 = no "))
diasDescanso = int(input("Dias de descanso -  1 = si  / 0 = no  "))

if vacaciones == 1:
    vacaciones = True
else:
    vacaciones = False

if diasDescanso == 1:
    diasDescanso = True
else:
    diasDescanso = False 


print(f'Vacaciones?: {vacaciones}')
print(f'Dias de descanso?: {diasDescanso}')

if not vacaciones and diasDescanso:
    print("No hay posibilidades de que pueda asistir al juego")
elif vacaciones or diasDescanso:
    print("Hay posibilidades de que pueda asistir al juego")
else:
    print("Puedo asistir al juego")