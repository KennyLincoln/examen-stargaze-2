from flask import render_template, redirect, request, session, flash
from flask_app import app
from flask_app.models.publicacion import Publicacion
from flask_app.models.usuario import Usuario

@app.route('/dashboard')
def dashboard():
    if 'usuario_id' not in session:
        return redirect('/')

    usuario = Usuario.get_by_id({'id': session['usuario_id']})
    publicaciones = Publicacion.obtener_publicaciones(session['usuario_id'])
    return render_template('dashboard.html', usuario=usuario, publicaciones=publicaciones)

@app.route('/crear/publicacion', methods=['POST'])
def crear_publicacion():
    if 'usuario_id' not in session:
        return redirect('/')

    if not Publicacion.validar_publicacion(request.form):
        return redirect('/dashboard')

    datos = {
        "nombre": request.form['nombre'],
        "lugar": request.form['lugar'],
        "fecha": request.form['fecha'],
        "descripcion": request.form['descripcion'],
        "usuario_id": session['usuario_id']
    }
    Publicacion.guardar(datos)
    return redirect('/dashboard')

@app.route('/editar/<int:id>')
def editar_publicacion(id):
    if 'usuario_id' not in session:
        return redirect('/')

    publicacion = Publicacion.get_by_id({'id': id})
    if not publicacion:
        return redirect('/dashboard')

    if publicacion.usuario_id != session['usuario_id']:
        return redirect('/dashboard')

    return render_template('editar_publicacion.html', publicacion=publicacion)

@app.route('/actualizar/publicacion/<int:id>', methods=['POST'])
def actualizar_publicacion(id):
    if 'usuario_id' not in session:
        return redirect('/')

    publicacion = Publicacion.get_by_id({'id': id})
    if not publicacion or publicacion.usuario_id != session['usuario_id']:
        return redirect('/dashboard')

    if not Publicacion.validar_publicacion(request.form, publicacion):
        return redirect(f'/editar/{id}')

    datos = {
        "id": id,
        "lugar": request.form['lugar'],
        "fecha": request.form['fecha'],
        "descripcion": request.form['descripcion']
    }
    Publicacion.actualizar(datos)
    return redirect('/dashboard')

@app.route('/borrar/<int:id>')
def borrar_publicacion(id):
    if 'usuario_id' not in session:
        return redirect('/')

    publicacion = Publicacion.get_by_id({'id': id})
    if publicacion and publicacion.usuario_id == session['usuario_id']:
        Publicacion.borrar({'id': id})

    return redirect('/dashboard')

@app.route('/me_gusta/<int:id>', methods=['POST'])
def me_gusta(id):
    if 'usuario_id' not in session:
        return redirect('/')

    Publicacion.agregar_me_gusta({
        "usuario_id": session['usuario_id'],
        "publicacion_id": id
    })
    return redirect('/dashboard')