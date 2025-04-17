from flask import Flask
from . import auth_bp

def create_app():
    app = Flask(__name__)

    # Registrar el Blueprint de autenticación
    app.register_blueprint(auth_bp, url_prefix='/auth')

    return app
