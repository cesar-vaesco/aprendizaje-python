"""
El método __init__ es un método especial de una clase en Python. El objetivo fundamental del método __init__ 
es inicializar los atributos del objeto que creamos.
"""

# Encapsular el valor de los atributos de la clase


class Persona:
    # Atribuitos de clase
    def __init__(self, nombre, apellido, edad):
        self._nombre = nombre
        self._apellido = apellido
        self._edad = edad

    #  Declaración de métodos getters
    @property
    def nombre(self):
        return self._nombre

    @property
    def apellido(self):
        return self._apellido

    @property
    def edad(self):
        return self._edad

    # Declaración de métodos setter
    @nombre.setter
    def nombre(self, nombre):
        self._nombre = nombre

    @apellido.setter
    def apellido(self, apellido):
        self._apellido = apellido

    @edad.setter
    def edad(self, edad):
        self._edad = edad

    # la palabra self pasa la referencia de los valores asignados a los atributos de la clase
    # Uso de getter para mostrar los datos de los atributos de los objetos instanciados
    def mostrar_detalle(self):
        return f"""
                    - Nombre: {self._nombre} 
                    - Apellido: {self._apellido} 
                    - Edad: {self._edad}
                """


# --> Fin del ambito de la clase Persona

persona1 = Persona("Verónica", "Cortez", 43)
persona2 = Persona("Vanessa", "Varela Corrales", 15)

# print(persona1.nombre())

# Uso de métodos set para modificar valores de los atributos
persona1.nombre = "Veróniquilla"
persona1.apellido = "Cordoba Juaréz"
persona1.edad = 18


print(persona1.mostrar_detalle())
# print(persona2.mostrar_detalle())
