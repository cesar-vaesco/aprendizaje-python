# Convertir clase en clase abstracta
from abc import ABC, abstractmethod


class FiguraGeometrica:
    def __init__(self, ancho, alto):
        if self._validar_valor(ancho):
            # if 0 < ancho < 10:
            self._ancho = ancho
        else:
            self._ancho = 0
            print(f"Valor erroneo ancho: {ancho}")

        if self._validar_valor(alto):
            # if 0 < alto < 10:
            self._alto = alto
        else:
            print(f"Valor erroneo alto: {alto}")
            self._alto = 0

    # Métodos Getters
    @property
    def ancho(self):
        return self._ancho

    @property
    def alto(self):
        return self._alto

    # Métodos Setters
    @ancho.setter
    def ancho(self, ancho):
        if self._validar_valor(ancho):
            self._ancho = ancho
        else:
            print(f"Valor erroneo ancho: {ancho}")

    @alto.setter
    def alto(self, alto):
        if self._validar_valor(alto):
            self._alto = alto
        else:
            print(f"Valor erroneo alto: {alto}")

    # Método abstracto
    @abstractmethod
    def calcular_area(self):
        pass

    # Método String str
    def __str__(self):
        return f"- Ancho: {self._ancho} - Alto: {self._alto}"

    def _validar_valor(self, valor):
        return True if 0 < valor < 10 else False


# Probar clase

if __name__ == "__main__":
    fg1 = FiguraGeometrica(9, 5)

    print(fg1)
