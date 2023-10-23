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
            sentencia = 'SELECT * FROM persona'
            cursor.execute(sentencia)
            print("Selecionamos las filas de la tabla persona usando cursor.fetchall")
            registros_persona = cursor.fetchall()

            print("Impresión de cada fila según el valor de las columnas")
            for row in registros_persona:
                print("Nombre = ", row[0], )
                print("Apellido = ", row[1])
                print("Correo  = ", row[2], "\n")
except Exception as e:
    print(f"Ocurrio un error: {e}")
finally:
    print("Cerrando cursor")