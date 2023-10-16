class DispositivoEntrada:
    def __init__(self, tipo_entrada, marca):
        self.tipo_entrada = tipo_entrada
        self.marca = marca

    def __str__(self):
        return f"- Tipo Entrada: {self.tipo_entrada} \n- Marca: {self.marca}"



if __name__ == "__main__":
    
    dE1 = DispositivoEntrada("Mouse", "Dell")
    
    print(dE1)