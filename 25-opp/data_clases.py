from dataclasses import dataclass
from typing import ClassVar


@dataclass
class Persona:
    nombre: str
    apellido: str = None
    contador_personas: ClassVar[int] = 0

    def __post_init__(self):
        if not self.nombre:
            raise ValueError(f"Valor nombre vacío: {self.nombre}")
        if self.nombre:
            Persona.contador_personas += 1


persona1 = Persona("Juan", "Peréz")
print(f"{persona1!r}")
print(persona1)

# Variable de clase
print(f"Variable de clase: {Persona.contador_personas}")
# Variables de instancia
print(f"{persona1.__dict__}")
#  Variable con valores vacíos
persona_vacia = Persona("Joaquín", "")
print(f"Persona vacía: {persona_vacia}")
print(f"Variable de clase: {Persona.contador_personas}")
