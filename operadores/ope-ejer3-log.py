num1 = int(input("Ingresa primer numero...  "))
num2 = int(input("Ingresa segundo numero...  "))

if num1 > num2:
    print("Número 1 es mayor")
    print(f"{num1} es mayor que {num2}")
elif num1 < num2:
    print("Número 2 es mayor")
    print(f"{num1} es menor que {num2}")
else:
    print(f'{num1} es igual a {num2}')