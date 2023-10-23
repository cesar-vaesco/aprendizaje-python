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
        with conexion.cursor() as cursor:
            sentencia = 'SELECT * FROM persona ORDER BY id_persona'
            cursor.execute(sentencia)
            print("Selecionamos las filas de la tabla persona usando cursor.fetchall\n")
            registros_persona = cursor.fetchall()

            print("Impresión de cada fila según el valor de las columnas\n")
            for row in registros_persona:
                print("Id = ", row[0], )
                print("Nombre = ", row[1], )
                print("Apellido = ", row[2])
                print("Correo  = ", row[3], "\n")
except Exception as e:
    print(f"Ocurrio un error: {e}")
finally:
    print("Cerrando cursor")