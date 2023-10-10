class Vehiculo:
    def __init__(self, color, ruedas):
        self.color = color
        self.ruedas = ruedas

    def __str__(self):
        return f"Color: {self.color} - Ruedas: {self.ruedas}"


if __name__ == "__main__":
    vehiculo1 = Vehiculo("Rojo", 4)

    print(vehiculo1)
