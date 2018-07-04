import os

class Config(object):
    # A good pattern is to obtain configuration settings from environment variables
    # when in a production environment but to use a default value during development.
    SECRET_KEY = os.environ.get("SECRET_KEY") or "you-will-never-guess"
