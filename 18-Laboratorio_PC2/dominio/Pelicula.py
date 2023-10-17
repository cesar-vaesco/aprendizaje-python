class Pelicula:
    def __init__(self, nombre):
        self._nombre = nombre

    def __str__(self):
        return f"Pelicula: {self.nombre}"

    # Definición de métodos getters y setters

    @property
    def nombre(self):
        return self._nombre
    
    @nombre.setter
    def nombre(self, nombre):
        self._nombre = nombre
     
if __name__ == "__main__":
    peli = Pelicula("Batman")

    print(f"{peli}")


