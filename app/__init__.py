import flask

app = flask.Flask(__name__)

# Put this import here to avoid circular imports.
from app import routes

