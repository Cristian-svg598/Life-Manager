from flask import Flask
from flask_cors import CORS
from flask_jwt_extended import JWTManager
from dotenv import load_dotenv
import os
from app.extensions import db  
from app.routes.auth_route import auth_bp  

load_dotenv()

def create_app():
    app = Flask(__name__)

    app.config['SECRET_KEY'] = os.getenv('SECRET_KEY')
    app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DATABASE_URL')
    app.config['JWT_SECRET_KEY'] = os.getenv('JWT_SECRET_KEY')  

    db.init_app(app)
    CORS(app)
    JWTManager(app)

    app.register_blueprint(auth_bp, url_prefix='/auth')  

    return app
