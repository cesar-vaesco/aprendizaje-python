
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
            sentencia = 'SELECT * FROM persona'
            # la entrada se convierte en una tupla de tuplas
            cursor.execute(sentencia)
            registro = cursor.fetchone()
            
            print(registro)
except Exception as e:
    print(f"Ocurrio un error: {e}")
finally:
    print(f"\nCerrando conexion....\n")
    conexion.close()