class Product:
    def __init__(self, x, y) -> None:
        self._x = x
        self._y = y

    def display(self):
        return f"x: {self._x} - y: {self._y}"

    @property
    def value(self):
        return self._x

    @value.setter
    def value(self, val):
        self._x = val

    @value.deleter
    def value(self):
        del p1.value
        return "Value deleter"


p1 = Product(5, 10)

print(p1.value)



print(f"{p1.value}")


# class Product:
#     def __init__(self, x, y) -> None:
#         self._x = x
#         self._y = y

#     def display(self):
#         return f"x: {self._x} - y: {self._y}"

#     @property
#     def get_x(self):
#         return self._x

#     @get_x.setter
#     def set_x(self, x):
#         self._x = x

#     @property
#     def get_y(self):
#         return self._y

#     @get_y.setter
#     def set_y(self, y):
#         self._y = y


# p = Product(5, 10)

# print(p.display())
# print(f"Valor actual de x: {p.get_x}")
# p.set_x = 15
# print(f"Valor actual de x: {p.get_x}")
# print(f"Valor actual de y: {p.get_y}")
# p.set_y = 65
# print(f"Valor actual de y: {p.get_y}")
# print(p.display())


#     def __init__(self):
#         # atributo inicialiado de acceso público
#         self.data1 = 10
#         # atributo inicializado de acceso privado( convención )
#         self._data2 = 20
#         # atributo inicializado de sólo acceso a tráves de la clase
#         self.__data3 = 30

#     def methodA(self):
#         return f"Soy un método público y llamo el valor de un atributo público: {self.data1}"

#     def _methodB(self):
#         return f"Soy un método privado por convención llamando el valor de un atributo privado por convención: {self._data2}"

#     def __methodC(self):
#         return f"""
# Método declarado bajo el contexto de una clase,
# llamando un atributo declarado bajo el contexto de una clase: {self._Product__data3}
# """


# p1 = Product()


# print(dir(p1))
# print(p1.data1)
# print(p1._data2)
# print(p1._Product__data3)
# print(p1.methodA())
# print(p1._methodB())
# print(p1._Product__methodC())
