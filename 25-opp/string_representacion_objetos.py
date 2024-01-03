# Representación de objetos (str, repr, format)

# print(dir(object))


class Persona:
    def __init__(self, nombre, apellido) -> None:
        self.nombre = nombre
        self.apellido = apellido

    def __repr__(self) -> str:
        # return f"Persona(nombre:{self.nombre}, apellido: {self.apellido})"
        return f"{self.__class__.__name__}(nombre:{self.nombre}, apellido: {self.apellido})"


persona1 = Persona("Juan", "Pérez")

print(persona1)
# Se asegura que se manda llamar el método repr
print(f"Mi objeto persona1: {persona1!r}")
