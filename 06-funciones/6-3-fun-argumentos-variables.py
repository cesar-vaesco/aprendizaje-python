# Declaración de función
# El asterisco en el paso de argumentos permite
# crear una tupla y agregar de forma indistinta
# valores pasando como parametros


def listar_nombres(*nombres):
    for nombre in nombres:
        print(nombre)


listar_nombres("César", "Veronica", "Gloria")
listar_nombres("Aurelio", "Vanessa", "Maki")
