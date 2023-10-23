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
            sentencia = "DELETE FROM persona WHERE id_persona = %s"
            # Se solicita a usuario el id del registro a eliminar
            entrada = input("Proporciona el id_persona a eliminar:   ")
            #  pasamos el valor a una tupla
            valores = (entrada,)
            cursor.execute(sentencia, valores)
            registros_eliminados = cursor.rowcount
            print(f"Registro actualizado: {registros_eliminados}")
            
except Exception as e:
    print(f"Ocurrio un error: {e}")
finally:
    print("Cerrando cursor...")