# Representación de objetos (str, repr, format)

# print(dir(object))


class Persona:
    def __init__(self, nombre, apellido) -> None:
        self.nombre = nombre
        self.apellido = apellido

    # repr, más enfocado a los programadores
    def __repr__(self) -> str:
        # return f"Persona(nombre:{self.nombre}, apellido: {self.apellido})"
        return f"{self.__class__.__name__}(nombre:{self.nombre}, apellido: {self.apellido})"

    # str, es más para el usuario final o inclusive para otros sistemas
    def __str__(self):
        return f"{self.__class__.__name__}: {self.nombre} {self.apellido}"

    # Se manda a llamar al usar un f-string
    def __format__(self, __format_spec: str) -> str:
        return f"{self.__class__.__name__} con nombre {self.nombre} y apellido {self.apellido}"


persona1 = Persona("Juan", "Pérez")

print(persona1)
# Se asegura que se manda llamar el método repr
print(f"Mi objeto persona1: {persona1!r}")
# Método repr llamado de manera explicita
print(persona1.__repr__())
# Str
print(persona1.__str__())
# Por default se manda llamar str
print(persona1)
# Formar por default ,manda llamar al método str
print(f"{persona1}")
