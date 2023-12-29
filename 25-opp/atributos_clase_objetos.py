class Persona:
    contador_personas = 0

    def __init__(self, nombre, apellido):
        self.nombre = nombre
        self.apellido = apellido


# Mostrar atributos de un objeto
persona1 = Persona("Juan", "Peréz")
print(persona1.__dict__)

# Crear un atributio al vuelo
print(persona1.contador_personas)
# No es posible modificarlo con el objetp, sino con la clase
persona1.contador_personas = 10
print(persona1.__dict__)

print(f"Atributo de clase: {Persona.contador_personas}")
print(f"Atributo de objeto: {persona1.contador_personas}")

persona2 = Persona("Hermi", "Negrete")
print(persona2.__dict__)
print(persona2.contador_personas)

# Asociar un atributo de clase al vuelo
Persona.contador_personas2 = 20
print(f"Atributo de clase creado al vuelo: {Persona.contador_personas2}")
