from flask import Flask
from flask_sqlalchemy import SQLAlchemy
#from config import Config
#print('--->', Config.SQLALCHEMY_DATABASE_URI)

db = SQLAlchemy()

def create_app():
    app = Flask(__name__)
    app.config.from_object('config.Config')
    db.init_app(app)
    
    return app