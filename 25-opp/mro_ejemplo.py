class Clase1:
    def __init__(self) -> None:
        print("Clase1.__init__")

    def metodo(self):
        print("Método Clase1")


class Clase2(Clase1):
    def __init__(self) -> None:
        print("Clase2.__init__")
        super().__init__()

    def metodo(self):
        print("Método Clase2")
        super().metodo()


class Clase3(Clase1):
    def __init__(self) -> None:
        print("Clase3.__init__")
        super().__init__()

    def metodo(self):
        print("Método Clase3")
        super().metodo()


class Clase4(Clase2, Clase3):
    def metodo(self):
        print("Método Clase4")
        super().metodo()


clase4 = Clase4()

# __bases__
print(Clase4.__bases__)
# __mro__
print(Clase4.__mro__)
# Cúal método se ejecuta?
clase4.metodo()
