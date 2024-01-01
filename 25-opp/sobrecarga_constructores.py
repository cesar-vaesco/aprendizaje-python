# Simulación de sobrecarga de constructores
# Otras formas de crear objetos


class Persona:
    def __init__(self, nombre, apellido) -> None:
        self.nombre = nombre
        self.apellido = apellido

    @classmethod
    def crear_persona_vacia(cls):
        return cls(None, None)

    @classmethod
    def crear_persona_con_valores(cls, nombre, apellido):
        return cls(nombre, apellido)

    def __str__(self) -> str:
        return f"- Nombre: {self.nombre} - Apellido: {self.apellido}"


persona1 = Persona("Juan", "Pérez")
persona_vacio = Persona.crear_persona_vacia()
persona_valores = Persona.crear_persona_con_valores("Ale", "López")

print(persona1)
print(persona_vacio)
print(persona_valores)
