#from flask import Flask
from flask_api import FlaskAPI

app = FlaskAPI(__name__)
# Initialize the app
#app = Flask(__name__, instance_relative_config=True)

# Load the views
from app import views

# Load the config file
app.config.from_object('config')