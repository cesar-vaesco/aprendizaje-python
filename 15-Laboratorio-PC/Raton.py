from DispositivoEntrada import DispositivoEntrada


class Raton(DispositivoEntrada):
    contador_ratones = 0

    def __init__(self, _marca, _tipo_entrada):
        Raton.contador_ratones += 1
        self._id_raton = Raton.contador_ratones
        super().__init__(_marca, _tipo_entrada)

    def __str__(self):
        return f"\n\t- Id_Ratón: {self._id_raton} \n\t- Marca:{self.marca} \n\t- Entrada:{self.tipo_entrada}"
    
    
if __name__ == "__main__":
    raton1 = Raton("Mouse", "Dell")
    raton2 = Raton('HP', 'USB')
    raton3 = Raton('Acer', 'Bluetooth')
    print(raton1)
    print(raton2)
    print(raton3)