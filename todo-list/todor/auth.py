from flask import Blueprint, render_template, request, url_for, redirect, flash, session, g
from werkzeug.security import generate_password_hash, check_password_hash
from .models import User
from . import db

bp = Blueprint('auth', __name__, url_prefix='/auth')

@bp.route('/register', methods=('GET', 'POST'))
def register():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        # Creamos objetos con los datos
        user = User(username, generate_password_hash(password))

        error = None

        # Consulta a la bd
        user_name = User.query.filter_by(username=username).first()
        if user_name is None:
            # Agregamos el usuario a la sesión y realizamos el commit para guardarlo en la base de datos
            db.session.add(user)
            db.session.commit()
            return redirect(url_for('auth.login'))
        else:
            error = f'El usuario {username} ya esta registrado'
            flash(error)

    return render_template('auth/register.html')


@bp.route('/login', methods=('GET', 'POST'))
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        error = None

        #Validar datos
        user = User.query.filter_by(username=username).first()
        if user == None:
            error = 'Nombre de usuario incorrecto'
        elif not check_password_hash(user.password, password):
            error = 'Contraseña incorrecta'

        #Iniciar sesion
        if error is None:
            session.clear()
            session['user_id'] = user.id
            return redirect(url_for('todo.index'))

        flash(error)
    return render_template('auth/login.html')

#Para que se ejecute la funcion en cada peticion
@bp.before_app_request
#Mantener sesion iniciada
def load_logged_in_user():
    #recuperar id con el cual inicia el usuario
    user_id = session.get('user_id')

    if user_id is None:
        g.user = None
    else:
        #si existe id obtenemos dato de la bd
        g.user = User.query.get_or_404(user_id)

@bp.route('/logout')
#Cerrar sesion
def logout():
    session.clear()
    return redirect(url_for('index'))

import functools

def login_required(view):
    #Si la vista requiere inicio de sesion la capturamos, y verificamos si el usuario esta logueado 
    @functools.wraps(view)
    def wrapped_view(**kwargs):
        if g.user is None:
            return redirect(url_for('auth.login'))
        return view(**kwargs)
    
    return wrapped_view