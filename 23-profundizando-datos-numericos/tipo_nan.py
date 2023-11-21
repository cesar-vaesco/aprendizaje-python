import math
from decimal import Decimal 
# NaN = Not a Number (no es un número)
# NaN no es sencible a mayusculas
# NaN es un valor númerico para representar un número indefinido
a = float("NaN")
print(f"a: {a}")
print(f"Es NaN (not a number)?: {math.isnan(a)}")

a = float("2.0")
print(f"a: {a}")
print(f"Es NaN (not a number)?: {math.isnan(a)}")

a = Decimal("NaN")

print(f"a: {a}")
print(f"Es NaN (not a number)?: {math.isnan(a)}")