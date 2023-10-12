class Producto:
    contador_productos = 0

    def __init__(self, nombre, precio):
        Producto.contador_productos += 1
        self._id_producto = Producto.contador_productos
        self._nombre = nombre
        self._precio = precio

    # Getters
    @property
    def nombre(self):
        return self._nombre

    @property
    def precio(self):
        return self._precio

    # Setters
    @nombre.setter
    def nombre(self, nombre):
        self._nombre = nombre

    @precio.setter
    def precio(self, precio):
        self._precio = precio

    def __str__(self):
        return f"\n*Id: {self._id_producto} *Nombre producto: {self._nombre} *Precio producto: {self._precio}"


if __name__ == "__main__":
    producto1 = Producto("Jabón", 20.0)
    producto2 = Producto("Papel", 45.0)
    producto3 = Producto("Aceite", 63.0)
    producto4 = Producto("Frijol", 50.0)

    print(producto1)
    print(producto2)
    print(producto3)
    print(producto4)
