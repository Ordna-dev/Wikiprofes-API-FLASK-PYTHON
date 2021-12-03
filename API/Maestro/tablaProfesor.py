from conexionBaseDatos import cursor, bd

def contieneDigitos(inputString):
    return any(char.isdigit() for char in inputString)

def contieneSimbolos(text: str) -> bool:
    return any(c for c in text if not c.isalnum() and not c.isspace())

def existeProfesor(nombre, apellidos):
    query = "SELECT COUNT(*) FROM maestro.maestros WHERE nombre = %s AND apellidos = %s"
    cursor.execute(query, (nombre, apellidos))
    if cursor.fetchone()[0] == 1:             #Evalua la existencia del usuario mediante el correo
        return True                              
    else:
        return False

def crearProfesor(centro, nombre, apellidos):
   if existeProfesor(nombre, apellidos) == True:
       return False
   else:
        if contieneDigitos(centro) or contieneDigitos(nombre) or contieneDigitos(apellidos):
            return False
        elif contieneSimbolos(centro) or contieneSimbolos(nombre) or contieneSimbolos(apellidos):
            return False
        elif centro == "" or nombre == "" or apellidos == "":
            return False
        insertar = "INSERT INTO maestro.maestros (promedio_conocimiento, promedio_puntualidad, promedio_dificultad, numero_evaluaciones, centro_universitario, nombre, apellidos, id_usuario) VALUES(%s, %s, %s, %s, %s, %s, %s, %s)"
        cursor.execute(insertar, (None, None, None, '0', centro, nombre, apellidos, None))
        bd.commit() 
        if cursor.rowcount:
            return True
        else:
            return False

def getProfesores():
     query = "SELECT nombre, apellidos, promedio_conocimiento, promedio_puntualidad, promedio_dificultad, centro_universitario FROM maestro.maestros"
     cursor.execute(query)
     maestros = []
     for row in cursor.fetchall():
         maestro = {
             'nombre': row[0],
             'apellidos': row[1],
             'promedio_conocimiento': row[2],                           #Obtener informacion de todos los profesores registrados.
             'promedio_puntualidad': row[3],                              
             'promedio_dificultad': row[4],
             'centro_universitario': row[5]
         }
         maestros.append(maestro)
     return maestros

def buscarProfesor(patron):
    if contieneDigitos(patron):
        return "Los digitos, simbolos y el texto vacio no son validos"
    elif contieneSimbolos(patron):
        return "Los digitos, simbolos y el texto vacio no son validos"
    elif patron == "":
        return "Los digitos, simbolos y el texto vacio no son validos"
    query = "SELECT * FROM maestro.maestros WHERE nombre || ' ' || apellidos LIKE %s"
    cursor.execute(query, ('%'+patron+'%',))
    maestros = []
    for row in cursor.fetchall():
         maestro = {
            'promedio_conocimiento': row[1],                           #Obtener informacion de todos los profesores registrados.
            'promedio_puntualidad': row[2],                              
            'promedio_dificultad': row[3],
            'numero_evaluciones': row[4],
            'centro_universitario': row[5],
            'nombre': row[6],
            'apellidos': row[7],
            'id_usuario': row[8]
         }
         maestros.append(maestro)
    return maestros

def consultarMaestro(id):
    query = "SELECT * FROM maestro.maestros WHERE id_maestro = %s"
    cursor.execute(query, (id,))
    maestros = []
    for row in cursor.fetchall():
        maestro = {
        'promedio_conocimiento': row[1],                           #Obtener informacion de todos los profesores registrados.
        'promedio_puntualidad': row[2],                              
        'promedio_dificultad': row[3],
        'numero_evaluciones': row[4],
        'centro_universitario': row[5],
        'nombre': row[6],
        'apellidos': row[7],
        'id_usuario': row[8]
        }
        maestros.append(maestro)
    return maestros
