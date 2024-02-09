from decouple import config
import os
from datetime import timedelta

from dotenv import load_dotenv

load_dotenv()

BASE_DIR = os.path.dirname(os.path.realpath(__file__))

class Config:
    SECRET_KEY = os.getenv("SECRET_KEY", "secret")
    SQLALCHEMY_TRACK_MODIFICATIONS = os.getenv("SQLALCHEMY_TRACK_MODIFICATIONS", False)

class ProdConfig(Config):
    SQLALCHEMY_DATABASE_URI = os.getenv("DATABASE_URI", "sqlite:///prod.db")
    DEBUG = os.getenv("DEBUG", False)
    SQLALCHEMY_ECHO = os.getenv("ECHO", False)
    SQLALCHEMY_TRACK_MODIFICATIONS = os.getenv("SQLALCHEMY_TRACK_MODIFICATIONS", False)

# Combine all the tables into a single SQLite database file
os.environ["DATABASE_URI"] = "sqlite:///prod.db"
os.environ["DEBUG"] = "False"
os.environ["ECHO"] = "False"

# Initialize the Flask-SQLAlchemy extension with the ProdConfig configuration
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config.from_object(ProdConfig)
db = SQLAlchemy(app)

# Defining models
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), unique=True, nullable=False)
    password = db.Column(db.String(128), nullable=False)

    def __repr__(self):
        return f'<User {self.username}>'

# Initialize the database with the ProdConfig configuration
db.create_all()