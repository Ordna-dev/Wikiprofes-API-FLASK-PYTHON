from conexionBaseDatos import cursor, bd

def existeModerador(correo):
    query = "SELECT COUNT(*) FROM usuario.usuarios WHERE correo_electronico = %s"
    cursor.execute(query, (correo,))

    if cursor.fetchone()[0] == 1:
        return True
    else: 
        return False

def asignarModerador(correo, id):
    if existeModerador(correo) == True:
        return False
    else:

        insertar = "INSERT INTO usuario.usuarios_moderador (usuarios_moderador_pkey) VALUES(%s)"

        cursor.execute(insertar, (id))
        bd.commit()

        if cursor.rowcount:
            return True
        else:
            return False