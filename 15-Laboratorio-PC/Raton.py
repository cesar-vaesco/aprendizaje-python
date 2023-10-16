class Raton:
    contador_ratones = 0

    def __init__(self):
        Raton.contador_ratones += 1
        self.id_raton = Raton.contador_ratones

    def __str__(self):
        return f"Id_Ratón: {self.contador_ratones}"
    
    
if __name__ == "__main__":
    raton1 = Raton();
    
    print(raton1)