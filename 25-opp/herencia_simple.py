# Ejemplo de herencia simple


class ListaSimple:
    def __init__(self, elementos) -> None:
        self._elementos = list(elementos)

    def agregar(self, elemento):
        self._elementos.append(elemento)

    def __getitem__(self, indice):
        return self._elementos[indice]

    def ordenar(self):
        self._elementos.sort()

    def __len__(self):
        return len(self._elementos)

    def __repr__(self) -> str:
        return f"- Nombre de la clase: {self.__class__.__name__} \n\t- Contenido de la lista: {self._elementos!r}"


class ListaOrdenada(ListaSimple):
    def __init__(self, elementos=[]) -> None:
        super().__init__(elementos)
        # Ordenamos los elementos una vez inicializado
        self.ordenar()

    def agregar(self, elemento):
        super().agregar(elemento)
        # Ordenamos el nuevo elemento
        self.ordenar()


# Lista sólo acepta números
class ListaEnteros(ListaSimple):
    def __init__(self, elementos=[]) -> None:
        for elemento in elementos:
            self._validar(elemento)
        #  Una validados los elementos los agregamos
        super().__init__(elementos)
        self.ordenar()

    def _validar(self, elemento):
        # Se valida sí el elemento es del tipo entero
        if not isinstance(elemento, int):
            raise ValueError(f"No es un valor entero")

    # Se sobreescribe método agregar de la clase padre
    def agregar(self, elemento):
        self._validar(elemento)
        super().agregar(elemento)


# Lista de enteros ordenada
class ListaEnterosOrdenada(ListaEnteros, ListaOrdenada):
    pass


lista = [5, 3, 8, 6]
lista_simple = ListaSimple(lista)


print(lista_simple)
lista_simple.agregar(12)
print(lista_simple)
print(lista_simple.__getitem__(3))
print(lista_simple.__len__())

lista_ordenada = ListaOrdenada([4, 3, 6, 9, 10, -1])

print(lista_ordenada)
lista_ordenada.agregar(-14)
print(lista_ordenada)
print(lista_ordenada.__len__())

lista_enteros = ListaEnteros([5, 6, 9, 12, 48, -12])
print(lista_enteros)

lista_enteros_ordenada = ListaEnterosOrdenada([4, 5, -1, 10, 14, -4])
print(lista_enteros_ordenada)
lista_enteros_ordenada.agregar(-20)
print(lista_enteros_ordenada)
# Saber las clases padre y su orden
print(ListaEnterosOrdenada.__bases__)
# MRO Method Resolution Order
print(ListaEnterosOrdenada.__mro__)


print("Es entero?", isinstance(10, int))
print("Es una cadena?", isinstance("10", str))
print(
    "Es lista enteros ordenada?",
    isinstance(lista_enteros_ordenada, ListaEnterosOrdenada),
)

print("Es lista enteros? ", isinstance(lista_enteros_ordenada, ListaEnteros))
print(
    "Es lista enteros enteros?",
    isinstance(lista_enteros_ordenada, ListaEnteros),
)
print("Es lista ordenada?", isinstance(lista_enteros_ordenada, ListaOrdenada))
print(
    "Es de varios tipos: ",
    isinstance(
        lista_enteros_ordenada,
        (ListaEnteros, ListaEnterosOrdenada, ListaOrdenada, ListaSimple, object),
    ),
)
