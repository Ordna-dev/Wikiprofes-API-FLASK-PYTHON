from flask import Flask, json, request, redirect, render_template, jsonify
from API.Usuario.tablaUsuario import crearUsuario, iniciarSesionUsuario
from API.Materia.tablaMateria import registrarMateria
from API.Maestro.tablaProfesor import crearProfesor, getProfesores, buscarProfesor, consultarMaestro
from API.Maestro.tablaComenterio import insertarComentario, consultarComentarios
from API.Materia.tablaMateria import consultarMateria
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
            data = request.get_json()
            nombreUsuario = data["nombreUsuario"]
            correo = data["correo"]                           
            key = data["pass"]
            keyConfirm = data["repass"]
            if key == keyConfirm:
                if crearUsuario(nombreUsuario, correo, key) == False:
                    return jsonify({"code": "singin error"})
                return jsonify({"code" : "Ok"})
        except:
            return jsonify({"Code:": "Input error"})

@app.route('/api/login', methods=['POST'])
def login():
    if request.method == 'POST' and request.is_json:
        try:
            data = request.get_json()
            correo = data['correo_electronico']
            contra = data['acces_key']
            id, ok = iniciarSesionUsuario(correo, contra)
            if ok:
                return jsonify({"code": "ok", "id": id})
            else:
                return jsonify({"code": "credenciales invalidas"})
        except:
            return jsonify({"code": "error"})

@app.route('/api/logout', methods=['UNLOCK'])
def logout():
    if request.method == 'UNLOCK':
        return jsonify({"Code:": "Saliste de tu cuenta"})

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

@app.route('/api/registrarProfesor', methods = ['POST', 'GET'])
def registrarProfesor(id=None):
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

    elif request.method == "GET" and id == None:
        return jsonify(getProfesores())

@app.route('/api/usuarios/<int:id>/search', methods = ['GET']) #este seria para cuando se este logeado
@app.route('/api/search', methods = ['GET'])
def busquedaPorPatron():
    if request.method == "GET":
        try:
            data = request.get_json()
            patron = data['patron']
            maestros = []
            maestros = buscarProfesor(patron)
            if maestros:
                return jsonify(maestros)
            else:
                return jsonify({"result": "sin coincidencia"})
        except:
            return jsonify({"code": "Input error"})

@app.route('/api/maestros/<int:id>', methods = ['GET'])
def recuperarMaestro(id):
    if request.method == "GET":
        try:
            maestro = consultarMaestro(id)
            if maestro:
                return jsonify(maestro)
            else:
                return jsonify({"code": "sin coincidencia"}) 
        except:
            return jsonify({"code": "Error desconocido"})

@app.route('/api/usuarios/<int:id_usuario>/maestros/<int:id_maestro>/comentarios', methods = ['POST'])
def realizarComentario(id_usuario, id_maestro):
    if request.method == "POST":
        try:
            data = request.get_json()
            anonimo = data['anonimo']
            comentario = data['comentario']
            id_materia = data['id_materia']
            caso, resultado = insertarComentario(id_usuario, id_maestro, anonimo, comentario, id_materia)
            if caso == None and resultado == True:
                return jsonify({"code":"ok"})
            elif resultado == False:
                if caso == 1:
                    return jsonify({"code":"El profesor no imparte la materia"})
                elif caso == 2:
                    return jsonify({"code":"Se ha comentado previamente"})
                elif caso == 3:
                    return jsonify({"code":"Desconocido"})
        except:
            return jsonify({"code":"input error"})

@app.route('/api/maestros/<int:id>/comentarios', methods = ['GET'])
def comentariosProfesor(id_maestro):
    if request.method == "GET":
        comentarios = consultarComentarios(id_maestro)
        if comentarios: 
            nombre_materia = consultarMateria(comentarios["id_materia"])
            comentarios["nombre_materia"] = nombre_materia
            return jsonify(comentarios)

    return jsonify({"code": "error consulta"})
