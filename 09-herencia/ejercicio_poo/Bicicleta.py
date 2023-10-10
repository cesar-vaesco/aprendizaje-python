from Vehiculo import Vehiculo


class Bicicleta(Vehiculo):
    def __init__(self, color, ruedas, tipo):
        super().__init__(color, ruedas)
        self.tipo = tipo

    def __str__(self):
        return (
            f"Caracteristicas de bicicleta:\n \t-Tipo: {self.tipo} - {super().__str__()} "
        )


if __name__ == "__main__":
    bicicleta1 = Bicicleta("Azul", 2, "Montaña")
    print(bicicleta1)
