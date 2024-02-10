import os
from flask import Flask, Blueprint, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_bcrypt import Bcrypt
from flask_jwt_extended import JWTManager
from flask_cors import CORS
from datetime import timedelta

app = Flask(__name__)
CORS(app, origins="http://localhost:5173")

# my configs
app.config['SECRET_KEY'] = '266ceaf6c1874e0484d761f1360708eb'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///myapp.db'
app.config['JWT_SECRET_KEY'] = '0126766336ea640fa941e53a'

# my instances
db = SQLAlchemy(app)
bcrypt = Bcrypt(app)
migrate = Migrate(app, db)
jwt = JWTManager(app)


flask_db_init = Blueprint('flask_db_init', __name__)

@app.before_first_request
def create_tables():
    db.create_all()

app.register_blueprint(flask_db_init)

# your Flask app code here