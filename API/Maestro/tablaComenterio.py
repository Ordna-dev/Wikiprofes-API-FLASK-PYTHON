from conexionBaseDatos import cursor, bd
from datetime import date

def verificarProfesor_Materia(id_materia, id_maestro):
    query = "SELECT COUNT(*) FROM materia.materias_maestros WHERE id_materia = %s AND id_maestro = %s"
    cursor.execute(query, (id_materia, id_maestro))
    if cursor.fetchone()[0] == 1:
        return True
    
    return False


def unicidadComentario(id_usuario, id_maestro, id_materia):
    query = "SELECT COUNT(*) FROM maestro.comentarios WHERE id_usuario = %s AND id_maestro = %s AND id_materia = %s"
    cursor.execute(query, (id_usuario, id_maestro, id_materia))
    if cursor.fetchone()[0] == 1:
        return False
    
    return True

def insertarComentario(id_usuario, id_maestro, anonimo, comentario, id_materia):
    if verificarProfesor_Materia(id_materia, id_maestro) == True:
        if unicidadComentario(id_usuario, id_maestro, id_materia) == True:
            fecha = date.today()
            insertar = "INSERT INTO maestro.comentarios(fecha, anonimo, id_usuario, id_maestro, comentario, id_materia) VALUES(%s, %s, %s, %s, %s, %s)"
            cursor.execute(insertar, (fecha, anonimo,id_usuario, id_maestro, comentario, id_materia))
            bd.commit()
            if cursor.rowcount:
                return None, True
            else:
                return 3, False
        else:
            return 2, False
    else:
        return 1, False

def consultarComentarios(id_maestro):
    query = "SELECT * FROM maestro.comentarios WHERE id_maestro = %s"
    cursor.execute(query, (id_maestro,))
    comentarios = []
    if cursor.fetchone()[0] == 1:
        for row in cursor.fetchall():
            comentario = {
                'fecha': row[1],                           #Obtener informacion de todos los profesores registrados.
                'anonimo': row[2],  
                'comentario': row[6],
                'id_materia': row[7]
            }
            comentarios.append(comentario)
    print(comentarios)
    return comentarios

