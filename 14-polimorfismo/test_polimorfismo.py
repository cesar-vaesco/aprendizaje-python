from Empleado import Empleado
from Gerente import Gerente


def imprimir_detalles(objeto):
    # print(objeto)
    print(type(objeto))
    print(objeto.mostrar_detalles())

    # Se valida si el objeto es una instancia de clase
    # isinstance recibe como argumentos una instancia y una clase y regresar un booleano(True o False)
    if isinstance(objeto, Gerente):
        print(objeto.departamento)


empleado = Empleado("Juan", 5000)
gerente = Gerente("Raúl", 4500, "RRHH")


imprimir_detalles(empleado)
imprimir_detalles(gerente)
