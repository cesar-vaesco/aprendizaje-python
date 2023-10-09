"""
El método __init__ es un método especial de una clase en Python. El objetivo fundamental del método __init__ 
es inicializar los atributos del objeto que creamos.
"""


class Persona:
    # Atribuitos de clase
    def __init__(self, _nombre, _apellido, _edad):
        self.nombre = _nombre
        self.apellido = _apellido
        self.edad = _edad

# la palabra self pasa la referencia de los valores asignados a los atributos de la clase
    def mostrar_detalle(self):
        return f"""
- Nombre: {self.nombre} 
- Apellido: {self.apellido} 
- Edad: {self.edad} 
                """


# Inicializando un objeto de la clase
persona1 = Persona("César", "Vargas", 43)

persona2 = Persona("Verónica", "Cortez", 43)


print(
    f"""
    --- Objeto 1 ---
    Nombre: {persona1.nombre}
    Apellido: {persona1.apellido}
    Edad: {persona1.edad}
    """
)


print("\nCambiando los valores del objeto 1")

persona1.nombre = "Gloria"
persona1.apellido = "Vargas Cortez"
persona1.edad = 22

print(persona1.mostrar_detalle())
print(persona2.mostrar_detalle())
