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
            sentencia = "UPDATE persona SET nombre = %s, apellido=%s, email=%s WHERE id_persona = %s"
            valores=('Claudio','De la O', 'cdela@correo.com',9)
            cursor.execute(sentencia, valores)
            registro_actualizado = cursor.rowcount
            print(f"Registro actualizado: {registro_actualizado}\n")
            
            
except Exception as e:
    print(f"Ocurrio un error: {e}")
finally:
    print("Cerrando cursor...")