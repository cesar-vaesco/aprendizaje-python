from Conexion import Conexion
from Persona import Persona
from logger_base import log


class PersonaDAO:
    """
    DAO = Data Access Object
    """

    _SELECCIONAR = 'SELECT * FROM persona ORDER BY id_persona'
    _INSERTAR = 'INSERT INTO persona(nombre, apellido, email) VALUES (%s, %s, %s)'
    _ACTUALIZAR = 'UPDATE persona SET nombre=%s, apellido=%s, email=%s WHERE id_persona=%s'
    _ELIMINAR = 'DELETE FROM persona WHERE id_persona=%s'

    @classmethod
    def seleccionar(cls):
        with Conexion.obtenerCursor() as cursor:
            cursor.execute(cls._SELECCIONAR)
            registros = cursor.fetchall()

            personas = []

            for registro in registros:
                persona = Persona(registro[0], registro[1], registro[2], registro[3])
                personas.append(persona)
            return personas

    @classmethod
    def insertar(cls, persona):
        with Conexion.obtenerConexion() as conexion:
            with Conexion.obtenerCursor() as cursor:
                valores = (persona.nombre, persona.apellido, persona.email)
                cursor.execute(cls._INSERTAR, valores)
                log.debug(f"Persona insertada: {persona}")
                return cursor.rowcount

    @classmethod
    def actualizar(cls, persona):
        with Conexion.obtenerConexion():
            with Conexion.obtenerCursor() as cursor:
                valores = (
                    persona.nombre,
                    persona.apellido,
                    persona.email,
                    persona.id_persona,
                )
                cursor.execute(cls._ACTUALIZAR, valores)
                log.debug(f'Persona actualizada: {persona}')
                return cursor.rowcount

    @classmethod
    def eliminar(cls, persona):
        with Conexion.obtenerConexion():
            with Conexion.obtenerCursor() as cursor:
                # Espera una tupla por eso el id_persona es seguido por una coma
                valores = (persona.id_persona,)
                cursor.execute(cls._ELIMINAR, valores)
                log.debug(f'Registro eliminado: {persona}')
                return cursor.rowcount

if __name__ == "__main__":

# Insertar un registro
    # persona1 = Persona(nombre="Ricardo", apellido="Maldonado", email="rima@correo.com")
    # personas_insertadas = PersonaDAO.insertar(persona1)
    # log.debug(f"Personas insertadas: {personas_insertadas}")

# Actualizar registro
    # persona2 = Persona(68,"Lau", "Vega", "lave@correo.com")
    # personas_actualizadas = PersonaDAO.actualizar(persona2)
    # log.debug(f"Personas actualizados: {personas_actualizadas}")


# Eliminar registros
    persona = Persona(id_persona=46)
    personas_eliminadas = PersonaDAO.eliminar(persona)
    log.debug(f"Eliminadas: {personas_eliminadas}")

# Listar registros
    personas = PersonaDAO.seleccionar()
    for persona in personas:
        log.info(persona)

