# Proporcionar mes del año y determinar la estación a la que corresponde

print("\tMes y estación del año\n")


mes = int(input("Proporciona el mes del año (númerico) "))
mes_nombre = ""
estacion = ""
if mes == 1:
    mes_nombre = "Enero"
    estacion = "Invierno"
elif mes == 2:
    mes_nombre = "Febrero"
    estacion = "Invierno"
elif mes == 3:
    mes_nombre = "Marzo"
    estacion = "Invierno"
elif mes == 4:
    mes_nombre = "Abril"
    estacion = "Primavera"
elif mes == 5:
    mes_nombre = "Mayo"
    estacion = "Primavera"
elif mes == 6:
    mes_nombre = "Junio"
    estacion = "Primavera"
elif mes == 7:
    mes_nombre = "Julio"
    estacion = "Verano"
elif mes == 8:
    mes_nombre = "Agosto"
    estacion = "Verano"
elif mes == 9:
    mes_nombre = "Septiembre"
    estacion = "Verano"
elif mes == 10:
    mes_nombre = "Octubre"
    estacion = "Otoño"
elif mes == 11:
    mes_nombre = "Noviembre"
    estacion = "Otoño"
elif mes == 12:
    mes_nombre = "Diciembre"
    estacion = "Otoño"



"""
if mes == 1 or mes == 2 or mes == 3:
    estacion = "Invierno"
elif mes == 4 or mes == 5 or mes == 6:
    estacion = "Primavera"
elif mes == 7 or mes == 8 or mes == 9:
    estacion = "Verano"
elif mes == 10 or mes == 11 or mes == 12:
    estacion = "Otoño"
"""

if mes >=1 and mes <= 12:
    print(
        f"""
    El mes ingresado es {mes_nombre}.
    {mes_nombre} pertenece a la estación {estacion}
    """
    )
else:
    print("Valor ingresado erroneo")