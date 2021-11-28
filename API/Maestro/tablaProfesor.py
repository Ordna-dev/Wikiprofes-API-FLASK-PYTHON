from conexionBaseDatos import cursor, bd

def existeProfesor(nombre, apellidos):
    query = "SELECT COUNT(*) FROM maestro.maestros WHERE nombre = %s AND apellidos = %s"
    cursor.execute(query, (nombre, apellidos))
    if cursor.fetchone()[0] == 1:             #Evalua la existencia del usuario mediante el correo
        return True                              
    else:
        return False

def crearProfesor(nombre, apellidos):
   if existeProfesor(nombre, apellidos) == True:
       return False
   else:
       insertar = "INSERT INTO maestro.maestros (promedio_conocimiento, promedio_puntualidad, promedio_dificultad, centro_universitario, nombre, apellidos) VALUES(%s, %s, %s, %s, %s, %s)"
       cursor.execute(insertar, ('0', '0', '', '0', 'CUECI', '', nombre, apellidos))
       bd.commit() 
       if cursor.rowcount:
            return True
       else:
            return False

def getProfesores():
     query = "SELECT id_usuario, promedio_conocimiento, promedio_puntualidad, promedio_dificultad, centro_universitario FROM maestro.maestros"
     cursor.execute(query)
     maestros = []
     for row in cursor.fetchall():
         maestro = {
             'id_maestro': row[0],
             'promedio_conocimiento': row[1],                           #Obtener informacion de todos los profesores registrados.
             'promedio_puntualidad': row[2],                              
             'promedio_dificultad': row[3],
             'centro universitario': row[4]
         }
         maestros.append(maestro)
     return maestros


# def iniciarSesionProfesor(correo, contra):
#     h = hashlib.new("sha256", bytes(contra, "utf-8"))
#     h = h.hexdigest()
#     query = "SELECT id FROM maestro WHERE correo = %s AND user_key = %s"
#     cursor.execute(query, (correo, h))
#     consulta = cursor.fetchone()                            #Inicio de sesion del profesor(usuario) mediante correo y contraseña
#     if consulta:                                            #Esta parte del codigo no es necesaria?
#         maestro = {
#             'Id' : consulta[0],
#             'Nombre(s)' : consulta[1],
#             'Apellido(s)' : consulta[2],
#             'Correo' : consulta[3]
#         }
#         return maestro

#     else:
#         return False



# def modificar_profesor(id, columna, valor):
#     update = f"UPDATE maestro SET {columna} = %s WHERE id = %s"
#     cursor.execute(update, (valor, id))
#     bd.commit()

#     if cursor.rowcount:                                 #Modificar la informacion del profesor por si hubo algun error
#         return True
#     else: 
#         return False

# def eliminar_profesor(id):
#     eliminar = "DELETE from maestro WHERE id = %s"
#     cursor.execute(eliminar, (id,))
#     bd.commit()

#     if cursor.rowcount:                                 #Eliminar profesor(no usuario) de la base de datos por si hubo algun error
#         return True
#     else:
#         return False