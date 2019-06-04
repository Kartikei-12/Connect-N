"""API for Connect-N game"""

import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

from env import API_DB_NAME

db = SQLAlchemy()


def create_app():
    """"""
    app = Flask(__name__)
    app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///" + API_DB_NAME
    db.init_app(app)
    try:
        with open("connect_n/" + API_DB_NAME, "r") as f:
            pass
    except FileNotFoundError:
        print("Creating database")
        os.chdir("../")
        db.create_all()
    else:
        del f
    return app


app = create_app()

from routes import index

if __name__ == "__main__":
    app.run(debug=True)
