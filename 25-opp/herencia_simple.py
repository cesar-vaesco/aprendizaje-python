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


lista_simple = ListaSimple([5, 3, 6, 8])

print(lista_simple)
lista_simple.agregar(12)
print(lista_simple)
print(lista_simple.__getitem__(3))
print(lista_simple.__len__())
print(lista_simple.ordenar())

lista_ordenada = ListaOrdenada([4, 3, 6, 9, 10, -1])

print(lista_ordenada)
lista_ordenada.agregar(-14)
print(lista_ordenada)
print(lista_ordenada.__len__())
