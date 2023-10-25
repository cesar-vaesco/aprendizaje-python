from logger_base import log
from Conexion import Conexion

class CursorDelPool:
    # Método para crear las variables conexion y cursor
    def __init__(self):
        self._conexion = None
        self._cursor = None

    # Método que usa el objeto Conexion para crear un cursor
    def __enter__(self):
        log.debug("Inicio del metodo del with __enter___")
        self._conexion = Conexion.obtenerConexion()
        self._cursor = self._conexion.cursor()
        return self._cursor
    
    #  Se valida la transacción o se hace rollback de la conexion
    def __exit__(self, tipo_excepcion, valor_excepcion, detalle_excepcion):
        log.info("Se ejecuta método __exit__")
        if valor_excepcion:
            self._conexion.rollback()
            log.error(f"Ocurrio una excepcion, se hace rollback: {tipo_excepcion} - {valor_excepcion} - {detalle_excepcion}") 
        else:
            self._conexion.commit()
            log.debug("Commit de la transacción")
        self._cursor.close()
        
        Conexion.liberarConexion(self._conexion)