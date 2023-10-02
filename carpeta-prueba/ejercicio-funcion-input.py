# Califica tu día del 1 al 10

califica = input("Califica tu día del 1 al 10...")

califica = int(califica)

if califica > 10 or califica < 1:
    print("Calificaste tu día con un valor fuera de rango")
else:
    print("A mí día lo califico con un ", califica)
