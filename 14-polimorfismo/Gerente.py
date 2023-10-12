from Empleado import Empleado


class Gerente(Empleado):
    def __init__(self, nombre, sueldo, departamento):
        super().__init__(nombre, sueldo)
        self.departamento = departamento

    def __str__(self):
        return f"Gerente [Departamento: {self.departamento}] {super().__str__()}"


if __name__ == "__main__":
    gerente1 = Gerente("José", 5000, "Supervición")
    gerente2 = Empleado("Raúl", 6500)

    print(f"Empleado: {gerente2}")
    print(f"Empleado: {gerente1}")
