from DispositivoEntrada import DispositivoEntrada


class Raton(DispositivoEntrada):
    contador_ratones = 0

    def __init__(self, tipo_entrada, marca):
        Raton.contador_ratones += 1
        super().__init__(tipo_entrada, marca)
        self.id_raton = Raton.contador_ratones

    def __str__(self):
        return f"{super().__str__()}\n\t- Id_Ratón: {self.contador_ratones} "
    
    
if __name__ == "__main__":
    raton1 = Raton("Mouse", "Dell");
    
    print(raton1)