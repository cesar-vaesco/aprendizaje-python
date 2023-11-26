class Product:
    def __init__(self):
        # atributo inicialiado de acceso público
        self.data1 = 10
        # atributo inicializado de acceso privado( convención )
        self._data2 = 20
        # atributo inicializado de sólo acceso a tráves de la clase
        self.__data3 = 30

    def methodA(self):
        return f"Soy un método público y llamo el valor de un atributo público: {self.data1}"

    def _methodB(self):
        return f"Soy un método privado por convención llamando el valor de un atributo privado por convención: {self._data2}"

    def __methodC(self):
        return f"""
Método declarado bajo el contexto de una clase, 
llamando un atributo declarado bajo el contexto de una clase: {self._Product__data3}
"""


p1 = Product()


print(dir(p1))
print(p1.data1)
print(p1._data2)
print(p1._Product__data3)
print(p1.methodA())
print(p1._methodB())
print(p1._Product__methodC())
