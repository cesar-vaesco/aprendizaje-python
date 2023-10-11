class Persona:
    contador_personas = 0

    def __init__(self, nombre, edad):
        Persona.contador_personas += 1

        self.id_persona = Persona.contador_personas
        self.nombre = nombre
        self.edad = edad

    def __str__(self):
        return f"Id: {self.id_persona} - Nombre: {self.nombre} - Edad: {self.edad}"


persona1 = Persona("Jacinto", 42)
persona2 = Persona("Jaci", 42)
persona3 = Persona("Joaquí", 35)

print(persona1)
print(persona2)
print(persona3)
print(f"Instancias de clase: {Persona.contador_personas}")