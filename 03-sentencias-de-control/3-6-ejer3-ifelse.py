calificacion = int(input("Ingrese su calificación\n\t"))

calificacion_final = ""

if calificacion == 10:
    calificacion_final = "A"
elif calificacion <= 9 and calificacion >= 8:
    calificacion_final = "B"
elif calificacion <= 8 and calificacion >= 7:
    calificacion_final = "C"
elif calificacion <= 7 and calificacion >= 6:
    calificacion_final = "D"
elif calificacion > 0 and calificacion < 6:
    calificacion_final = "F"
else:
    print("Error de asignación - Valor incorrecto")


print(f"Valor asignado: {calificacion} - Calificación: {calificacion_final}")
