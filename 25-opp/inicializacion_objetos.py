# Orden de inicialización de objetos


class Padre:
    def __init__(self) -> None:
        print("Inicializador clase Padre")

    def metodo(self):
        print("Método clase Padre")


class Hijo(Padre):
    # Se manda llamar el método init sí la clase hija no tiene su propio método
    def __init__(self) -> None:
        # De forma opcional se puede llamar el método init de la clase padre
        print("Inicializado clase Hijo")
        super().__init__()

    # Se sobreescribe el método heredado de la clase padre
    def metodo(self):
        print("Método clase Hijo")
        super().metodo()


# padre1 = Padre()
# padre1.metodo()

hijo = Hijo()
hijo.metodo()
