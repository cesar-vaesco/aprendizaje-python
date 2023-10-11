class FiguraGeometrica:
    def __init__(self, ancho, alto):
        self._ancho = ancho
        self._alto = alto

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
        self._ancho = ancho

    @alto.setter
    def alto(self, alto):
        self._alto = alto

    # Método String str
    def __str__(self):
        return f"- Ancho: {self._ancho} - Alto: {self._alto}"


# Probar clase

if __name__ == "__main__":
    fg1 = FiguraGeometrica(10, 5)

    print(fg1)
