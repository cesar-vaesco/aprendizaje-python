import psycopg2 as db

print("Creando conexión.... \n")

# Base de datos creada perviamente en postgrest
conexion = db.connect(
    user = "postgres",
    password = "admin",
    host = "127.0.0.1",
    port = "5432",
    database = "test_db"
    )

print(f"Datos de conexión: {conexion}\n")

# with realiza commit de forma automática la realización de la transacción
try:
    with conexion:
        with conexion.cursor() as cursor:
            sentencia = 'INSERT INTO persona (nombre, apellido, email) values (%s,%s,%s)'
            valores = ('Selina','Gómez', 'sego@correo.com')
            cursor.execute(sentencia, valores)
            
            sentencia = 'UPDATE persona SET nombre = %s, apellido = %s, email = %s WHERE id_persona = %s'
            valores= ('Sergio','Molina', 'semo@correo.com', 5)
            cursor.execute(sentencia, valores)
except Exception as e:
    conexion.rollback()
    print(f"Ocurrio un error, se hizo rollback de la transacción: {e}")
finally:
    print("Cerrando el cursor....")
    cursor.close()

print("Termina la transacción, se hizo commit...")