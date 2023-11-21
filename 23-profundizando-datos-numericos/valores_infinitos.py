import math
from decimal import *

# Manejo de valores infinitos

# infinito_positivo = float(5)

print(f" Validando valores infinitos positivos ".center(8), "*")
infinito_positivo = float("inf")
print(f"Es infinito?: {math.isinf(infinito_positivo)}")


print(" Validando valores infinitos negativos ".center(80, "*"))
infinito_negativo = float("-inf")
print(f"infinito_negativo: {infinito_negativo}")
print(f"Es infinito?: {math.isinf(infinito_negativo)}")

print("Módulo Math: validando valores infinitos".center(80, "*"))
infinito_positivo = math.inf
print(f"infinito_positivo: {infinito_positivo}")
print(f"Es infinito?: {math.isinf(infinito_positivo)}")

print(" Módulo decimal: validando valores infinitos ".center(80, "*"))
infinito_positivo = Decimal("Infinity")
print(f"infinito_positivo: {infinito_positivo}")
print(f"Es infinito?: {math.isinf(infinito_positivo)}")

print(" Módulo decimal: validando valores infinitos negativos".center(80, "*"))
infinito_negativo = Decimal("-Infinity")
print(f"infinito_negativo: {infinito_negativo}")
print(f"Es infinito?: {math.isinf(infinito_negativo)}")
