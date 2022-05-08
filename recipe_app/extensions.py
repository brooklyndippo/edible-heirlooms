from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from recipe_app.config import Config

app = Flask(__name__)
app.config.from_object(Config)

db = SQLAlchemy(app)

###########################
# Authentication
###########################

# TODO: Add authentication setup code here!



