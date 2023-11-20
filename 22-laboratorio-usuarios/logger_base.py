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
    