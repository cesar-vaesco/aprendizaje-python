class MiClase:
    variable_clase = "Valor variable clase"
    contador = 0

    def __init__(self, variable_instancia):
        self.variable_instancia = variable_instancia
        MiClase.contador += 1


# Accediendo variable de clase


# Instancia de clase
mi_clase = MiClase("Valor variable de instancia")
mi_clase2 = MiClase("Segunda instancia")
print(f"Instancia de clase: {mi_clase.variable_instancia}")
print(f"Instancia de clase: {mi_clase.variable_instancia}")
# Un objeto puede acceder a una variable de clase
print(f"Variable de clase usada por una instancia: {mi_clase.variable_clase}")
print(f"Instancias de clase: {MiClase.contador}")
