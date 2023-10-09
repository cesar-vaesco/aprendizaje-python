# Para poder listar un diccionario


def listar_terminos(**kargs):
    for llave, valor in kargs.items():
        print(f"{llave} : {valor}")


diccionario = {
    "IDE": "Integrated Development Environment",
    "OOP": "Object Oriented Programming",
    "DBMS": "Database Management System",
}

listar_terminos(
    IDE="Integrated Development Environment", DBMS="Database Management System"
)

listar_terminos(
    OOP="Object Oriented Programming",
)
