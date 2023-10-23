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
            # En una tupla de tuplas se agregan los datos de los registros a módificar
            valores=(
                ('Claudio','De la O', 'cdela@correo.com',9),
                ('Maricruz','Salazar','msala@correo.com', 10)
                )
            # se cambia el método del objeto cursor de execute a executemany
            cursor.executemany(sentencia, valores)
            registro_actualizado = cursor.rowcount
            print(f"Registro actualizado: {registro_actualizado}\n")
            
            # Bloque de código opcional
            print("Selecionamos las filas de la tabla persona usando cursor.fetchall\n")
            sentencia = 'SELECT * FROM persona ORDER BY id_persona'
            cursor.execute(sentencia)
            registros_persona = cursor.fetchall()

            print("Impresión de cada fila según el valor de las columnas\n")
            for row in registros_persona:
                print("Id = ", row[0], )
                print("Nombre = ", row[1], )
                print("Apellido = ", row[2])
                print("Correo  = ", row[3], "\n")
            # Fin de código opcional 
            
except Exception as e:
    print(f"Ocurrio un error: {e}")
finally:
    print("Cerrando cursor...")