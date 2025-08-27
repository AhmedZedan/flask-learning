from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///market.db'
app.config['SECRET_KEY'] = '8cb61608b80eeeaa00f5b9d5'
db = SQLAlchemy(app)
bcrypt = Bcrypt(app)

from market import routes