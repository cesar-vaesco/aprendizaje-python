class Monitor:
    contador_monitores = 0

    def __init__(self, marca, tamanio):
        Monitor.contador_monitores += 1
        self._id_monitor = Monitor.contador_monitores
        self._marca = marca
        self._tamanio = tamanio

    def __str__(self):
        return f"\n\t- Id Monitor: {self._id_monitor} \n\t- Marca: {self._marca} \n\t- Tamaño: {self._tamanio}"


if __name__ == "__main__":

    monitor = Monitor("Dell", "14 pulgadas")
    monitor1 = Monitor('HP', 15)
    monitor2 = Monitor('Acer', 27)
    print(monitor)
    print(monitor1)
    print(monitor2)
