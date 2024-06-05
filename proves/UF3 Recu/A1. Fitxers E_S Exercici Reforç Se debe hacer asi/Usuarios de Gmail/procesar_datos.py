def obtener_usuarios_gmail(correos):
    usuarios = []
    for correo in correos:
        usuario = correo.split('@')[0]
        usuarios.append(usuario)
    return usuarios
