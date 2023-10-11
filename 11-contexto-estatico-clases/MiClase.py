class MiClase:
    # Atributos de clase
    variable_clase = "Valor variable clase"
    contador = 0

    # Método estatico -> se asocian a la clase

    @staticmethod
    def metodo_estatico():
        return f"Llamada de método estático(de clase): {MiClase.variable_clase}"

    def __init__(self, variable_instancia):
        self.variable_instancia = variable_instancia
        MiClase.contador += 1


#################################

# Accediendo variable de clase


# Instancia de clase
mi_clase = MiClase("Valor variable de instancia")
mi_clase2 = MiClase("Segunda instancia")

MiClase.variable_clase2 = "Variable clase 2"

print(f"Instancia de clase: {mi_clase.variable_instancia}")
print(f"Instancia de clase: {mi_clase.variable_instancia}")
# Un objeto puede acceder a una variable de clase
print(f"Variable de clase usada por una instancia: {mi_clase.variable_clase}")
print(f"Instancias de clase: {MiClase.contador}")

print(
    f"Variable clase de clase 2 accediendo desde instancia: {mi_clase.variable_clase2}"
)
print(f"Variable clase de clase 2 accediendo desde la clase: {MiClase.variable_clase2}")

print(f'Método de clase --> {MiClase.metodo_estatico()}')
