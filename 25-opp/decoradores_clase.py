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

    # Revisamos si cada parametro tiene un método property asociado
    for parametro in parametros_init:
        #  property es un valor de tipo built-in para preguntar si se esta ocupando el decorador de property
        es_metodo_property = isinstance(atributos.get(parametro), property)
        if not es_metodo_property:
            raise TypeError(
                f"No cuenta con el método property para el parametro que hemos proporcionado: {parametro}"
            )

    # Crear el método repr dinamicamente
    def metodo_repr(self):
        # Obtenemos el nombre de la clase dinámicamnete
        nombre_clase = self.__class__.__name__
        print(f"Nombre clase: {nombre_clase}")

        # Obtenemos los nombres de las propiedades y sus valores dinámicamente
        # Se utilizara una expresión generadora para crear
        generador_arg = (
            f"{nombre}={getattr(self, nombre)!r}" for nombre in parametros_init
        )

        # Lista del generador
        lista_arg = list(generador_arg)
        print(f"Lista del generador: {lista_arg}")
        # Creamos la cadena a partir de la lista de argumentos
        argumentos = ", ".join(lista_arg)
        print(f"Argumentos del método repr: {argumentos}")
        # Creamos la forma del método __repr__ sin su nombre
        resultado_metodo_repr = f"{nombre_clase} ({argumentos})"
        print(f"Resultado método repr:  {resultado_metodo_repr}")

        # return f"Resultado de ejecutar el método repr"
        return resultado_metodo_repr
        # Agregar dinamicamente el metodo repr a nuestra clase

    setattr(cls, "__repr__", metodo_repr)

    return cls


@decorador_repr
class Persona:
    def __init__(self, nombre, apellido, edad):
        print("2.- Se ejecuta el metodo inicializador")
        self._nombre = nombre
        self._apellido = apellido
        self._edad = edad

    @property
    def nombre(self):
        return self._nombre

    @property
    def apellido(self):
        return self._apellido

    @property
    def edad(self):
        return self._edad

    # def __repr__(self):
    # f"Persona(nombre = {self._nombre} - apellido={self._apellido})"


persona1 = Persona("Juan", "Perez", 25)
persona2 = Persona("Mina", "Cardona", 45)

print(f"{persona1}")
print(f"{persona2}")

# Tiene los métoos de propiedad, nombre, apellido, repr
print(dir(Persona))
#  Tiene el método repr sov¿breescrito
codigo_repr = inspect.getsource(persona1.__repr__)
# VErificar la sobreescritura del método repr
print(codigo_repr)
