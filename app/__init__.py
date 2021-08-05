from flask import Flask
from .config import DevConfig

#Initializing application
newsy = Flask(__name__, instance_relative_config = True)

#Setting up configuration
newsy.config.from_object(DevConfig)
newsy.config.from_pyfile('config.py')
newsy.config["SECRET_KEY"] = "12345678"

# Initializing Flask Extensions

from app import views
from app import error