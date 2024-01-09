# Permiten trasformar de manera programatica nuestra clase,
# es similar a los decoradores de funciones (es metaprogramación)


import inspect


def decorador_repr(cls):
    print("1.- Se ejecuta el decorador de nuestra clase")
    print(f"Recibimos el objeto de la clase: {cls.__name__}")
    # Revisamos los atributos de la clase con elmetodo vars
    atributos = vars(cls)
    for nombre, atributo in atributos.items():
        print(nombre, atributo)

    # Se revisa si se a sobreescrito el método __init__
    if "__init__" not in atributos:
        raise TypeError(f"{cls.__name__} no ha seobrescrito el método __init__")

    firma_init = inspect.signature(cls.__init__)
    print(f"Firma método __init__: {firma_init}")

    # Recuperamos los parametros excepto el primero que es self
    parametros_init = list(firma_init.parameters)[1:]
    print(f"Parametros init: {parametros_init}")

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
