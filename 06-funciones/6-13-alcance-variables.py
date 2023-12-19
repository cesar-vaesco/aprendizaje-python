# Alcance de Variables (scope)

var_global = "Variable global"


def imprimir():
    global var_global
    # Acceder a una variable global
    print(f"Variable global accedida desde una función: {var_global}")
    # Definir una variable local
    var_local = "Variable local"
    print(f"Variable local accedida desde la función: {var_local}")

    var_global = "Nuevo valor de la variable global"

    def imprimir_anidada():
        print(
            f"Imprimir variable local y variable global desde función anidada: {var_local} - {var_global}"
        )
        print(
            f"Modificando valor de la variable global usando la plabla reservada 'global'"
        )

    print(f"Variable global: {var_global}")

    imprimir_anidada()


imprimir()
print(f"Variable global fuera de función: {var_global}")
print(
    " No es posible acceder a variables locales fuera del contexto donde fue definida ".center(
        110, "*"
    )
)
