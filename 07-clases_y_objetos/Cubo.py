class Cubo:
    def __init__(self, _ancho, _alto, _profundidad):
        self.ancho = _ancho
        self.alto = _alto
        self.profundidad = _profundidad

    def calcular_volumen(self):
        return self.ancho * self.alto * self.profundidad

    def mostrar_resultados(self):
        return f"El volumen es: {self.calcular_volumen()}"


ancho = float(input("Ingresa el ancho del cubo:  "))
alto = float(input("Ingresa el alto del cubo:  "))
profundidad = float(input("Ingresa el profundidad del cubo:  "))

cubo1 = Cubo(ancho, alto, profundidad)

print(cubo1.mostrar_resultados())
