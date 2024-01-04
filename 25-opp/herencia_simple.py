# Ejemplo de herencia simple


class ListaSimple:
    def __init__(self, elementos) -> None:
        self._elementos = list(elementos)

    def agregar(self, elemento):
        self._elementos.append(elemento)

    def __getitem__(self, indice):
        return self._elementos[indice]

    def ordenar(self):
        self._elementos.sort(reverse=True)

    def __len__(self):
        return len(self._elementos)

    def __repr__(self) -> str:
        return f"- Nombre de la clase: {self.__class__.__name__} \n\t- Contenido de la lista: {self._elementos!r}"


lista_simple = ListaSimple([5, 3, 6, 8])

print(lista_simple)
lista_simple.agregar(12)
print(lista_simple)
print(lista_simple.__getitem__(3))
print(lista_simple.__len__())
print(lista_simple.ordenar())
