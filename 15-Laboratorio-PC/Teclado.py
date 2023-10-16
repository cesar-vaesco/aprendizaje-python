class Teclado:
    contador_teclados = 0

    def __init__(self):
        Teclado.contador_teclados += 1
        self.id_teclado = Teclado.contador_teclados

    def __str__(self):
        return f"Id Teclado: {self.id_teclado}"

if __name__ == "__main__":
    teclado1 = Teclado()
    teclado2 = Teclado()
    teclado3 = Teclado()
    teclado4 = Teclado()


