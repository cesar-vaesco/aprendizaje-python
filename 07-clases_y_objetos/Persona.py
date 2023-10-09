"""
El método __init__ es un método especial de una clase en Python. El objetivo fundamental del método __init__ 
es inicializar los atributos del objeto que creamos.
"""


class Persona:
    # Atribuitos de clase
    def __init__(self, _nombre, _apellido, _edad):
        self.nombre = _nombre
        self.apellido = _apellido
        self.edad = edad


# Inicializando un objeto de la clase
persona1 = Persona("César", "Vargas", 43)

# print(type(Persona))
# print(persona1.nombre)
# print(persona1.apellido)
# print(persona1.edad)

print(
    f"""
    Nombre: {persona1.nombre}
    Apellido: {persona1.apellido}
    Edad: {persona1.edad}
    """
)
