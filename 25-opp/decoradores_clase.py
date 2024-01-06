# Permiten trasformar de manera programatica nuestra clase,
# es similar a los decoradores de funciones (es metaprogramación)


def decorador_repr(cls):
    print("1.- Se ejecuta el decorador de nuestra clase")
    print(f"Recibimos el objeto de la clase: {cls.__name__}")
    return cls


@decorador_repr
class Persona:
    def __init__(self, nombre, apellido):
        print("2.- Se ejecuta el metodo inicializador")
        self._nombre = nombre
        self._apellido = apellido

    @property
    def nombre(self):
        return self._nombre

    @property
    def apellido(self):
        return self._apellido

    # def __repr__(self):
    # f"Persona({self._nombre} - {self._apellido})"


persona1 = Persona("Juan", "Perez")
