class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad


class Empleado(Persona):
    def __init__(self, nombre, edad, sueldo):
        # El método super permite traer los atributos de la clase padre
        super().__init__(nombre, edad)
        self.sueldo = sueldo


empleado1 = Empleado("José", "Juaréz", 5000)

print("")
print("Información de empleado".center(30, "*"))
print("")

print(f"Empleado: {empleado1.nombre}")
print(f"Edad: {empleado1.edad}")
print(f"Sueldo: {empleado1.sueldo}")
print("")
