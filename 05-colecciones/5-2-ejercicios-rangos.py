# sintaxis de range(inicio<opcional>,
# fin<requerido>, incfremento<opcional>)
print("Rango 0 a 10 con numeros divisibles entre 3")
for n in range(0, 10, 3):
    print("-", n)
print("\n Rango 0 a 10 con numeros divisibles entre 3")
for i in range(11):
    if i % 3 == 0:
        print("-", i)
print("\n")

print("Rango de 2 a 6")
for n in range(2, 7):
    print("-", n)
print("\n")

print("Crear un rango de 3 a 10 pero con incremento de 2 en 2")
for n in range(3, 10, 2):
    print("-", n)
