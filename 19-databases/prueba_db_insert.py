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
        with conexion.cursor() as cursor:
            # Se crea sentencía sql
            sentencia = 'INSERT INTO persona(nombre, apellido, email) VALUES (%s, %s, %s)'
            #  Se crea una tupla con los valores que se van a pasar a la sentencia
            valores = ('Carlos', 'Lara', 'clara@correo.com')
            # Se ejecuta el cursor pasando la sentencia y los valores para insertar el registro
            cursor.execute(sentencia, valores)
            # Se rescata en una variable los registros insertados
            registros_insertados = cursor.rowcount
            print(f"Registros insertados: {registros_insertados}")
            
except Exception as e:
    print(f"Ocurrio un error: {e}")
finally:
    print(f"\nCerrando conexion....\n")
    conexion.close()

"""
try:

    with conexion:
        # Se crea un cursor para poder  usar sentencias sql
        with conexion.cursor() as cursor:
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
"""