import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from dotenv import load_dotenv

# Load variables from .env file
load_dotenv()

app = Flask(__name__)
# app.config['SQLALCHEMY_DATABASE_URI'] = f"mysql+mysqlconnector://{os.getenv('USERNAME_MYSQL')}:{os.getenv('PASSWORD_MYSQL')}@{os.getenv('HOST_MYSQL')}/{os.getenv('DATABASE_MYSQL')}"
app.config['SQLALCHEMY_DATABASE_URI'] = f"postgresql+psycopg2://{os.getenv('USERNAME_POSTGRE')}:{os.getenv('PASSWORD_POSTGRE')}@{os.getenv('HOST_POSTGRE')}/{os.getenv('DATABASE_POSTGRE')}"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

from app import routes
