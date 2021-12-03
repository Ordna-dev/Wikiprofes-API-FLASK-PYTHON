from conexionBaseDatos import cursor, bd #Archivo de conexiones
import hashlib          #Añadi un poco de codigo de lo que no era login
from datetime import date, datetime

def existeUsuario(correo):
    query = "SELECT COUNT(*) FROM usuario.usuarios WHERE correo_electronico = %s"
    cursor.execute(query, (correo,))

    if cursor.fetchone()[0] == 1:             #Evalua la existencia del usuario mediante el correo
        return True                              
    else:
        return False

def crearUsuario(nombreUsuario, correo, key):
    if existeUsuario(correo) == True:
        return False
    
    elif nombreUsuario == "" or correo == "" or key == "":
        return False
    else:
        h = hashlib.new("sha256", bytes(key, "utf-8"))   #A compilarlo a ver si jala
        h = h.hexdigest()
        fechaRegistro = date.today()
        horaRegistro = datetime.now().time()  
        insertar = "INSERT INTO usuario.usuarios (nombre, apellidos,nombre_usuario, acces_key, fecha, hora, correo_electronico) VALUES(%s, %s, %s, %s, %s, %s, %s)"
        cursor.execute(insertar, (None, None, nombreUsuario, h, fechaRegistro, horaRegistro, correo)) 
        bd.commit()

        if cursor.rowcount:
            return True
        else:
            return False

def iniciarSesionUsuario(correo, contra):
    h = hashlib.new("sha256", bytes(contra, "utf-8"))
    h = h.hexdigest()
    query = "SELECT id_usuario FROM usuario.usuarios WHERE correo_electronico = %s AND acces_key = %s"
    cursor.execute(query, (correo, h))
    id = cursor.fetchone()                            
    if id:                                            
        return id[0], True                  
    return None, False

def add_evaluar_maestro(evaluación): 
    Promedio_conocimiento = evaluación['conocimiento']
    Promedio_puntualidad = evaluación['puntualidad']
    Promedio_dificultad = evaluación['dificultad']           
                                                           
    insertar = "INSERT INTO evaluación \
        (conocimiento, puntualidad, dificultad) \
        VALUES (%s, %s, %s)"

    cursor.execute(insertar, 
    (Promedio_conocimiento, Promedio_puntualidad, Promedio_dificultad))
    bd.commit()

    if cursor.rowcount:
        return True
    else: 
        return False
    