resultado = None


try:
    a = int(input("Primer número: "))
    b = int(input("Segundo número: "))
    resultado = a / b

# La clase de menor jerarquía de excepciones van al inicio de la llamada de las excepciones
except ValueError as ve:
    print(f"\nOcurrió un error: {ve} - {type(ve)}")
except ZeroDivisionError as zde:
    print(f"\nOcurrió un error: {zde} - {type(zde)}")
except TypeError as te:
    print(f"\nOcurrió un error: {te} - {type(te)}")
except Exception as e:
    print(f"\nOcurrió un error: {e} - {type(e)}")

print(f"\nResultado: {resultado}")
print("Continuamos...\n")
