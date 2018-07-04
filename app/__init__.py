import flask

import config

app = flask.Flask(__name__)
app.config.from_object(config.Config)

# Put this import here to avoid circular imports.
from app import routes
