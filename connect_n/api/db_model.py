# pylint: disable=no-member

from datetime import datetime

from api import db


class User(db.Model):
    """"""

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), nullable=False)
    last_request = db.Column(db.DateTime, default=datetime.utcnow, nullable=False)
