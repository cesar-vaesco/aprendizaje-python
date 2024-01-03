# Ejemplo atributos publicos, protegidos, privados


class MiClase:
    def __init__(self, publico, protegido, privado) -> None:
        self.publico = publico
        self._protegido = protegido
        self.__privado = privado


objeto = MiClase("Valor publico", "Valor protegido", "Valor privado")


print(f"Acceso al valor publico: {objeto.publico}")
# Módificar el valor publico
objeto.publico = "Nuevo valor publico"
print(f"Acceso al valor publico: {objeto.publico}")

# Acceso a valor protegido
#  Solo dentro de la misma clase o en una clase hija
print(objeto._protegido)
# Modificar atributo protegido
objeto._protegido = "Nuevo valor protegido"
print(objeto._protegido)

# No se puede acceder un atributo privado de forma directa

# Forma en la cual se puede acceder a los atributos privados
print(objeto._MiClase__privado)
# print(objeto.__privado)

objeto.__privado = "Nuevo valor privado"
print(objeto._MiClase__privado)
objeto._MiClase__privado = "Nuevo valor privado"
print(objeto._MiClase__privado)
