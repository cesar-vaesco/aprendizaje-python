from Producto import Producto
from Orden import Orden

producto1 = Producto("Camisa", 150.00)
producto2 = Producto("Pantalón", 350.00)

producto3 = Producto("Calcetines", 50.00)
producto4 = Producto("Brusa", 250.00)

print(producto1)
print(producto2)

productos1 = [producto1, producto2]
productos2 = [producto3, producto4]
productos3 = [producto1, producto3]

orden1 = Orden(productos1)
orden1.agregar_producto(producto3)
orden1.agregar_producto(producto4)
print(orden1)
print(f"Total de la orden 1: {orden1.calcular_total()}")

orden2 = Orden(productos3)
print(orden2)
print(f"Total de la orden 2: {orden2.calcular_total()}")

orden3 = Orden(productos2)
print(orden3)
print(f"Total de la orden 3: {orden3.calcular_total()}")
