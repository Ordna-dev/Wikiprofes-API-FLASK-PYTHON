from conexionBaseDatos import cursor, bd

def existeAdministrador(correo):
    query = "SELECT COUNT(*) FROM usuario.usuarios WHERE correo_electronico = %s"
    cursor.execute(query, (correo,))

    if cursor.fetchone()[0] == 1:
        return True
    else: 
        return False

