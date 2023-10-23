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
#    --> Inicia transacción
    conexion.autocommit = False
    
#     --> transacciones a ejecutar
    cursor = conexion.cursor()
    sentencia = 'INSERT INTO persona (nombre, apellido, email) values (%s,%s,%s)'
    valores = ('Toño','Perez', 'tope@correo.com')
    cursor.execute(sentencia, valores)
    
    sentencia = 'UPDATE persona SET nombre = %s, apellido = %s, email = %s WHERE id_persona = %s'
    valores= ('Jacobo','Mora', 'jamo@correo.com', 17)
    cursor.execute(sentencia, valores)
    
# --> Finalización de la transacción
    conexion.commit()
    print("Termina la transacción, se hizo commit...")
    
except Exception as e:
    conexion.rollback()
    print(f"Ocurrio un error, se hizo rollback de la transacción: {e}")
finally:
    print("Cerrando el cursor....")
    cursor.close()