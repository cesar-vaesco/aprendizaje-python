from UsuarioDao import UsuarioDAO
from logger_base import log
from Usuario import Usuario

opcion = None

while opcion != 5:
    print('Opciones: ')
    print('1. Mostrar usuario ')
    print('2. Agregar usuario ')
    print('3. Modificar usuario ')
    print('4. Eliminar usuario ')
    print('5. Salir... ')
    opcion = int(input('Escribe tu opción(1-5): '))
    if opcion == 1:
        usuarios = UsuarioDAO.seleccionar()
        for usuario in usuarios:
            log.info(usuario)
    elif opcion == 2:
        var_username = input("Inserte username: ")
        var_password = input("Ingrese paswword: ")
        usuario = Usuario(username = var_username,password= var_password)
        usuario_insertado = UsuarioDAO.insertar(usuario)
        log.info(f'Usuario insertado: {usuario_insertado}')
    elif opcion == 3:
        id_usuario_var = int(input('Escribe el id_usuario a modificar: '))
        username_var = input('Escribe el nuevo username: ')
        password_var = input('Escribe el nuevo password: ')
        usuario = Usuario(id_usuario_var, username_var, password_var)
        usuarios_actualizados = UsuarioDAO.actualizar(usuario)
        log.info(f'usuarios actualizados: {usuarios_actualizados}')
    elif opcion == 4:
        id_usuario_var = int(input('Escribe el id_usuario a eliminar: '))
        usuario = Usuario(id_usuario=id_usuario_var)
        usuarios_eliminados = UsuarioDAO.eliminar(usuario)
        log.info(f'usuarios eliminados: {usuarios_eliminados}')
else:
    log.info('Salimos de la aplicación...')
   
