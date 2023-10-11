# Atributos de clase
class MiClase:
    variable_clase = "Valor variable clase"
    contador = 0

    # Los métodos de clase pueden usar información de la clase -recibe referencias de la clase
    @classmethod
    def metodo_clase(cls):
        return f"Método de clase: {cls.variable_clase}"

    # Método estatico -> se asocian a la clase pero no recibe
    # información de la clase (no se puede usar atributos de la clase), no hay referencias de la clase
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

print("\nInstancia de clase ".center(50, "*"))

print(f"Instancia de clase: {mi_clase.variable_instancia}")
# Un objeto puede acceder a una variable de clase
print(f"Variable de clase usada por una instancia: {mi_clase.variable_clase}")

print("\nVariable de clase ".center(50, "*"))
print(f"Instancias de clase: {MiClase.contador}")

print(
    f"Variable clase de clase 2 accediendo desde instancia: {mi_clase.variable_clase2}"
)
print(f"Variable clase de clase 2 accediendo desde la clase: {MiClase.variable_clase2}")

print("\nMétodo de clase de contexto estático ".center(50, "*"))

print(f"Método de clase --> {MiClase.metodo_estatico()}")

print("\nMandando llamar método de clase ".center(50, "-"))
print(MiClase.metodo_clase())
