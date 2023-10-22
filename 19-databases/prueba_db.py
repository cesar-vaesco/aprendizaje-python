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

# Se crea un cursor para poder  usar sentencias sql 

cursor = conexion.cursor()
sentencia = 'SELECT * FROM persona'
cursor.execute(sentencia)
registros = cursor.fetchall()

print(f"Registros: \n{registros}")

cursor.close()
conexion.close()