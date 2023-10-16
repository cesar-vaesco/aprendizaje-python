from DispositivoEntrada import DispositivoEntrada 

class Teclado(DispositivoEntrada):
    contador_teclados = 0

    def __init__(self,tipo_entrada, marca):
        Teclado.contador_teclados += 1
        super().__init__(tipo_entrada, marca)
        self.id_teclado = Teclado.contador_teclados

    def __str__(self):
        return f"{super().__str__()}\n\t- Id Teclado: {self.id_teclado}"

if __name__ == "__main__":
    teclado1 = Teclado("Teclado", "Dell")
    teclado2 = Teclado("Teclado Mecanico", "Asus")
    teclado3 = Teclado("Teclado", "Logitech")
    teclado4 = Teclado("Teclado", "Apple")
    
    print(teclado1)


