class Color:
    def __init__(self, color):
        self._color = color

        # Método getter
        @property
        def color(self):
            return self._color

        # Método setter
        @color.setter
        def color(self, color):
            self._color = color

    def __str__(self):
        return f"- Color: {self._color}"


if __name__ == "__main__":
    color1 = Color("Rojo")

    print(color1)
