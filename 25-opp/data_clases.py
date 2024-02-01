from dataclasses import dataclass
from typing import ClassVar


@dataclass(eq=True, frozen=True)
class Domicilio:
    calle: str
    numero: int = 0


@dataclass(eq=True, frozen=True)
class Persona:
    nombre: str
    apellido: str
    domicilio: Domicilio
    contador_personas: ClassVar[int] = 0

    def __post_init__(self):
        if not self.nombre:
            raise ValueError(f"Valor nombre vacío: {self.nombre}")
        if self.nombre:
            Persona.contador_personas += 1


domicilio1 = Domicilio("Marte", 15)
domicilio2 = Domicilio("Mercurio", 105)

persona1 = Persona("Juan", "Peréz", domicilio1)
print(f"{persona1!r}")
print(persona1)

# Variable de clase
print(f"Variable de clase: {Persona.contador_personas}")
# Variables de instancia
print(f"{persona1.__dict__}")
#  Variable con valores vacíos
persona_vacia = Persona("Joaquín", "", domicilio2)
print(f"Persona vacía: {persona_vacia}")
print(f"Variable de clase: {Persona.contador_personas}")

# Revisar igualdad entre objetos dataclass
persona2 = Persona("Juan", "Peréz", domicilio1)
print(f"Objetos iguales?:  {persona1 == persona2}")
# Agregar esta clase a una colección
coleccion = {persona1, persona2}
# Parametro de @dataclass forzen = True
# coleccion[0].nombre = "Juan Carlos"
# print(coleccion)
# persona1.nombre = "Juan Carlos"
# print(coleccion)

print(f"Variable de clase: {Persona.contador_personas}")
