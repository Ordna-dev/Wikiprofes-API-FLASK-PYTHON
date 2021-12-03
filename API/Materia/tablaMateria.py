from conexionBaseDatos import bd, cursor

def existeMateria(claveMateria):
    query = "SELECT COUNT(*) FROM materia.materias WHERE clave_materia = %s"
    cursor.execute(query, (claveMateria,))
    if cursor.fetchone()[0] == 1:
        return True
    else:
        return False


def registrarMateria(claveMateria, nombre):
    if existeMateria(claveMateria) == True:
        return False
    else:
        insertar = "INSERT INTO materia.materias (clave_materia, nombre) VALUES (%s, %s)"
        cursor.execute(insertar, (claveMateria, nombre))
        bd.commit()

        if cursor.rowcount:
            return True
        else:
            return 

def consultarMateria(id_materia):
    query = "SELECT nombre FROM materia.materias WHERE id_materia = %s"
    cursor.execute(query, (id_materia, ))
    materia = None
    for row in cursor.fetchall():
        materia = row[0]
    return materia
