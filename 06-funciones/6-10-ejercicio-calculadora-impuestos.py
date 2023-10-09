"""
Crear función para calcular el total de pagos incluyendo impuesto aplicado

Formula: pago_total = paso_sin_impuesto + pago_sin_impuesto * (impuesto/100) 
"""


def calcular_impuesto(pago_sin_impuesto, impuesto):
    pago_total = pago_sin_impuesto + (pago_sin_impuesto * (impuesto / 100))
    return pago_total


pago_sin_impuesto = float(input("Ingrese pago sin impuesto: "))
impuesto = float(input("Proporcione el monto del impuesto: "))


pago_total = calcular_impuesto(pago_sin_impuesto, impuesto)

print(
    f"Pago sin impuesto: {pago_sin_impuesto} - Monto del impuesto: {impuesto} - Pago total: {pago_total}"
)
