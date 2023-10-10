from Vehiculo import Vehiculo


class Coche(Vehiculo):
    def __init__(self, color, ruedas, velocidad):
        super().__init__(color, ruedas)
        self.velocidad = velocidad

    def __str__(self):
        # return f"Velocidad: [{self.velocidad}] Color: [{super().self.color}] Ruedas: [{super().self.ruedas}]"
        return f"Caracteristicas de coche: \n\t-Velocidad: {self.velocidad} km/hr - {super().__str__()} "

    # def __str__(self):
    # return f"Empleado: [Sueldo: {self.sueldo}] {super().__str__()} "


if __name__ == "__main__":
    coche1 = Coche("Rojo", 4, 100)

    print(coche1)
