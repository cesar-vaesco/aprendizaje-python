"""
El método __init__ es un método especial de una clase en Python. El objetivo fundamental del método __init__ 
es inicializar los atributos del objeto que creamos.
"""


class Persona:
    # Atribuitos de clase
    def __init__(self, _nombre, _apellido, _edad, *_valores, **_terminos):
        self.nombre = _nombre
        self.apellido = _apellido
        self.edad = _edad
        self.valores = _valores
        self.terminos = _terminos

    # la palabra self pasa la referencia de los valores asignados a los atributos de la clase
    def mostrar_detalle(self):
        return f"""
- Nombre: {self.nombre} 
- Apellido: {self.apellido} 
- Edad: {self.edad}
- Calle: {self.valores}
- Frutas: {self.terminos} 
                """


# Inicializando un objeto de la clase
persona1 = Persona("César", "Varela", 43, "Av. Oyamel", 250, m="manzana", p="pera")
persona2 = Persona("Verónica", "Cortez", 43)
persona3 = Persona("Vanessa", "Varela Corrales", 15)


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
persona1.apellido = "Varela Corrales"
persona1.edad = 22
persona1.telefono = "556581111"

# Mandando llamar el méto mostrar_detalle usando
# la referencia de un objeto a traves la llamada de la clase
# -->  print(Persona.mostrar_detalle(persona3))

print(persona1.mostrar_detalle())
print(persona2.mostrar_detalle())
print(Persona.mostrar_detalle(persona3))

print(f"Telefono instancia 1:  {persona1.telefono}")
