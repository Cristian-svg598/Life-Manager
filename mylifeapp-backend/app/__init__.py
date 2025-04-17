from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
from flask_jwt_extended import JWTManager 
from dotenv import load_dotenv
import os


load_dotenv()

db = SQLAlchemy()

def create_app():
    app = Flask(__name__)

    # Cargar configuraciones de .env
    app.config['SECRET_KEY'] = os.getenv('SECRET_KEY')
    app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DATABASE_URL')
    app.config['JWT_SECRET_KEY'] = os.getenv('JWT_SECRET_KEY')  

    db.init_app(app)
    CORS(app)
    JWTManager(app)  

    return app
