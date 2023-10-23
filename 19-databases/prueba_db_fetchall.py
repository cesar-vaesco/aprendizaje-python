import psycopg2


# Base de datos creada perviamente en postgrest
conexion = psycopg2.connect(
    user = "postgres",
    password = "admin",
    host = "127.0.0.1",
    port = "5432",
    database = "test_db"
    )

# print(conexion)

try:

    with conexion:
        # Se crea un cursor para poder  usar sentencias sql
        with conexion.cursor() as cursor:
            #  Se puede buscar uno o varios Id, el resultado dependera de que exista o no el registro
            sentencia = 'SELECT * FROM persona WHERE id_persona IN %s'
            # llaves_primarias = ((1, 2, 3, 4),)
            entrada = input("Proporciona los id\'s a buscar (sepadados por comas)}:  ")
            # la entrada se convierte en una tupla de tuplas
            # El método split quita las comas de la entrada (satos proporcionados por el usuario)
            llaves_primarias = (tuple(entrada.split(',')),)
            cursor.execute(sentencia, llaves_primarias)
            registros = cursor.fetchall()
            for registro in registros:
                print(registro)
except Exception as e:
    print(f"Ocurrio un error: {e}")
finally:
    print(f"\nCerrando conexion....\n")
    conexion.close()