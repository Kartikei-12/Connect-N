"""API for Connect-N game"""

from datetime import datetime

# Flask module(s) and it's extentions
from flask import Flask, request
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy

# Environment variable(s)
from .env import API_DB_NAME, MINIMUM_REQUEST_DURATION

db = SQLAlchemy()
migrate = Migrate()


def create_app(api_db_name=API_DB_NAME):
    """App factory function which runs setup for Flask app"""
    app = Flask(__name__)
    app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite://" + api_db_name
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    app.config["DEBUG"] = True
    db.init_app(app)
    migrate.init_app(app, db)
    return app


app = create_app()

# pylint: disable=unused-wildcard-import
from .auth import *
from .routes import *
from .tokens import *
from .error import *
from .db_model import *


# Helpful when using flask shell command
@app.shell_context_processor
def make_shell_context():
    return {"db": db, "User": User}
