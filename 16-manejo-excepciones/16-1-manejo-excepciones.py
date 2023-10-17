resultado = None
a = "10"
b = 0

try:
    resultado = a / b

except Exception as e:
    print(f"\nOcurrió un error: {e}")

# except ZeroDivisionError as e:
#     print(f"\nOcurrió un error: {e}")
# except TypeError as e:
#     print(f"\nOcurrió un error: {e}")

print(f"\nResultado: {resultado}")
print("Continuamos...\n")
