from flask import Flask, json, request, redirect, render_template, jsonify
from API.Usuario.tablaUsuario import crearUsuario
from API.Materia.tablaMateria import registrarMateria
from API.Maestro.tablaProfesor import crearProfesor, getProfesores
from flask.helpers import url_for
from main import app
import psycopg2

@app.route('/api')
def paginaInicio():
    return jsonify({"Code": "Welcome"})
    # return render_template('/api/index.html')           #Redireccionar a la vista principal del proyecto

#probado
@app.route('/api/signin', methods = ["GET", "POST"])
def registrar():
    if request.method == "GET":
        return render_template('registro.html')
    if request.method == "POST":
        try:
            # nombreUsuario = request.form["nombreUsuario"]
            # correo = request.form["correo"]                           #Redireccionar al registro
            # key = request.form["pass"]
            # keyConfirm = request.form["repass"]
            data = request.get_json()
            nombreUsuario = data["nombreUsuario"]
            correo = data["correo"]                           #Redireccionar al registro
            key = data["pass"]
            keyConfirm = data["repass"]
            if key == keyConfirm:
                if crearUsuario(nombreUsuario, correo, key) == False:
                    return jsonify({"code": "singin error"})
                return jsonify({"code" : "Ok"})
                # return render_template('index.html') comentado para realizar pruebas
        except:
            return jsonify({"Code:": "Input error"})
            # return render_template('registro.html') comentado para realizar pruebas

# ?
@app.route('/api/login.html', methods=['GET', 'POST'])
def login():
    if request.method == 'POST' and 'correo_electronico' in request.form and 'key' in request.form:
        correo_electronico = request.form['correo_electronico']
        key = request.form['key']

        cursor = psycopg2.cursor(psycopg2.cursors.DictCursor)
        cursor.execute('SELECT * FROM usuario WHERE correo_electronico = %s AND key = %s', (correo_electronico, key,))
        cuenta = cursor.fetchone()

        if cuenta:
            sesion = []
            sesion['logeado'] = True
            sesion['id'] = cuenta['Id_usuario'] 
            #Se muestran como advertencia porque actuan como cookies, /r segun yo se muestra como advernencia porque no decias que era un dicccionario
            #puede que este mal la neta no lo se si es así quita mi declaración, pd: no se que sea una cookie
            sesion['correo_electronico'] = cuenta['correo_electronico']

            return 'Inicio de sesión exitoso!'
        
        else:
            msg = "Contraseña/Correo incorrectos"

    return render_template('index.html', msg=msg)

# ?
@app.route('/api/logout.html')
def logout():
    sesion = [ ]
    sesion.pop('logeado', None)
    sesion.pop('Id_usuario', None)
    sesion.pop('correo_electronico', None)

    return redirect(url_for('login'))

#probado
@app.route('/api/registrarMateria', methods = ['POST'])
def materiasRegistro():
    if request.method == "POST":
        try:
            data = request.get_json()
            claveMateria = data["claveMateria"]
            nombre = data["nombre"] 
            if registrarMateria(claveMateria, nombre) == False:
                return jsonify({"code" : "Registrar error"})
            return jsonify({"code" : "Ok"})
        except:
            return jsonify({"Code:": "Input error"})

#toy probando, deja ajustarlo en donde debe ir, este era el utlimo que andaba haciendo antier
# ?
@app.route('/api/registrarProfesor', methods = ['POST', 'GET'])
def registrarProfesor():
    if request.method == "POST" and request.is_json:
        try:
            data = request.get_json() 
            nombre = data['nombre'] 
            apellidos = data['apellidos'] 
            if crearProfesor(nombre, apellidos) == False:
                return jsonify({"code" : "Insersión error"})
            return jsonify({"code": "Ok"})
        except:
            return jsonify({"code" : "Input error"})

    elif request.method == "GET":
        return jsonify(getProfesores())

@app.route('/api/acerca.html')
def paginaAcerca():
    return render_template('acerca.html')               #Redireccionar a "Acerca de"

@app.route('/api/contacto.html')
def paginaContacto():
    return render_template('contacto.html')             #Redireccionar a "Contacto"

@app.route('/api/preguntas.html')
def paginaPreguntas():
    return render_template('preguntas.html')            #Redireccionar a "Preguntas"

@app.route('/api/infowiki.html')
def paginaInfo():
    return render_template('infowiki.html')             #Redireccionar a "Info wiki"