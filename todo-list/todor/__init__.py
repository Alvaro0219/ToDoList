from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

def create_app():
    app = Flask(__name__)

    # Configuracion del proyecto
    app.config.from_mapping(
        DEBUG=True,
        SECRET_KEY='dev',
        SQLALCHEMY_DATABASE_URI="sqlite:///todolist.db"
    )

    # Inicializar conexion a BD
    db.init_app(app)

    # Registrar blueprint
    from . import todo, auth  # Mover las importaciones aquí para evitar importacion circular
    app.register_blueprint(todo.bp)
    app.register_blueprint(auth.bp)

    # Vista principal
    @app.route('/')
    def index():
        return render_template('index.html')

    # Migrar modelos a la BD
    with app.app_context():
        from .models import User, Todo
        db.create_all()

    return app
