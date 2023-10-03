a = int(input("Ingrese valor numérico:   "))

if a % 2 == 0:
    print(f"El valor de a ({a}) es número par")
else:
    print(f"El valor de a ({a}) es número impar")


edad = int(input("Ingrese edad:   "))

if edad >= 18:
    print(f"Su edad es {edad}. Usted es mayor de edad")
elif edad < 18 or edad > 0:
    print(f"Su edad es {edad}. Usted no es mayor de edad")
else:
    print(f'{edad} no es un valor valuable')    