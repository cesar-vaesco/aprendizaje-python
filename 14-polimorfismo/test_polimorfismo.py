from Empleado import Empleado
from Gerente import Gerente


def imprimir_detalles(objeto):
    # print(objeto)
    print(type(objeto))
    print(objeto.mostrar_detalles())



empleado = Empleado("Juan", 5000)
gerente = Gerente("Raúl", 4500, "RRHH")


imprimir_detalles(empleado)
imprimir_detalles(gerente)