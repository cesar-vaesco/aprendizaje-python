import psycopg2

print("Creando conexión.... \n")

# Base de datos creada perviamente en postgrest
conexion = psycopg2.connect(
    user = "postgres",
    password = "admin",
    host = "127.0.0.1",
    port = "5432",
    database = "test_db"
    )

print(f"Datos de conexión: {conexion}\n")


try:
    with conexion:
        print("Creando cursor.... \n")
        with conexion.cursor() as cursor:
            # Se crea sentencía sql
            sentencia = 'INSERT INTO persona(nombre, apellido, email) VALUES (%s, %s, %s)'
            #  Se crea una tupla de tuplas con los valores que se van a pasar a la sentencia
            valores = (('Carlos', 'Lara', 'clara@correo.com'),
                       ('Daniela', 'Castro', 'dcastro@correo.com'),
                       ('Pietro', 'López', 'plopez@correo.com'))
            # Se ejecuta el cursor pasando la sentencia y los valores para insertar el registro
            cursor.executemany(sentencia, valores)
            # Se rescata en una variable los registros insertados
            registros_insertados = cursor.rowcount
            print(f"Registros insertados: {registros_insertados}")
            
except Exception as e:
    print(f"Ocurrio un error: {e}")
finally:
    print(f"\nCerrando conexion....\n")
    conexion.close()
