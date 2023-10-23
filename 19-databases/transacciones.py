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


try:
    # conexion.autocommit = False es un valor por default, 
    # sí se cambiara el valor a True, es un amala practica
    # ya que los errores se subirian a la base de datos
    conexion.autocommit = False
    cursor = conexion.cursor()
    sentencia = 'INSERT INTO persona (nombre, apellido, email) values (%s,%s,%s)'
    valores = ('Mario','Morales', 'mmora@correo.com')
    cursor.execute(sentencia, valores)
    # Se esta confirmando la ejecución de la transacción
    conexion.commit()
    print("Termina la transacción...")
    
except Exception as e:
    conexion.rollback()
    print(f"Ocurrio un error, se hizo rollback de la transacción: {e}")
finally:
    print("Cerrando el cursor....")
    cursor.close()