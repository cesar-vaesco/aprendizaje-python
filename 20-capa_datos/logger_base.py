import logging as log


log.basicConfig(level=log.DEBUG,
                format = '%(asctime)s:  %(levelname)s [%(filename)s:%(lineno)s] %(message)s',
                datefmt = '%I:%M:%S %p',
                handlers = [
                    log.FileHandler('capa_datos.log'),
                    log.StreamHandler()
                ])




if __name__ == '__main__':
    log.debug('\nMensaje a nivel debug')
    log.info('\nMensaje a nivel info')
    log.warning('\nMensaje a nivel warning')
    log.error('\nMensaje a nivel error')
    log.critical('\nMensaje a nivel critico')
    
    
    
"""
Logging es un medio de rastrear los eventos que ocurren cuando se ejecuta algún software. 
El desarrollador del software agrega llamadas de registro a su código para indicar que 
ciertos eventos han ocurrido. Un evento se describe mediante un mensaje descriptivo que 
puede contener opcionalmente datos variables (es decir, datos que son potencialmente 
diferentes para cada ocurrencia del evento). Los eventos también tienen una importancia 
que el desarrollador atribuye al evento; la importancia también puede llamarse el nivel o la severidad.
"""
