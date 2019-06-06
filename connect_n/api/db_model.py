"""Database Model(s) for Connect-N API"""

# Python module(s)
import os
import base64
from datetime import datetime, timedelta

from werkzeug.security import generate_password_hash, check_password_hash

# pylint: disable=no-member

from app import db


class User(db.Model):
    """User table defination"""

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), nullable=False)
    password_hash = db.Column(db.String(128))
    email = db.Column(db.String(120), index=True, unique=True)
    last_request = db.Column(db.DateTime, default=datetime.utcnow, nullable=False)
    token = db.Column(db.String(32), index=True, unique=True)
    token_expiration = db.Column(db.DateTime)

    def set_password(self, password):
        """Method used to set user password

        Args:
            password (str): Password set as password hash"""
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        """Method to check user password

        Args:
            password (str): Password to check against

        Returns:
            bool : True if correct password"""
        return check_password_hash(self.password_hash, password)

    def from_dict(self, data, new_user=False):
        """Method to read user from dictioary

        Args:
            data (dict): Must contain username, email and password fields
            new_user (bool): If new user registrations"""
        for field in ["username", "email"]:
            if field in data:
                setattr(self, field, data[field])
        if new_user and "password" in data:
            self.set_password(data["password"])

    def to_dict(self, include_email=False):
        """Provides dictionary representation of user

        Args:
            include_email: Wheather to include email

        Returns:
            dict : dictionary representation"""
        data = {
            "id": self.id,
            "username": self.username,
            "last_request": self.last_request.isoformat() + "Z",
        }
        if include_email:
            data["email"] = self.email
        return data

    def get_token(self, expires_in=3600):
        """Token generator

        Args:
            expires_in (int): Seconds in which token expires

        Returns:
            str : API token for the user"""
        now = datetime.utcnow()
        if self.token and self.token_expiration > now + timedelta(seconds=60):
            return self.token
        self.token = base64.b64encode(os.urandom(24)).decode("utf-8")
        self.token_expiration = now + timedelta(seconds=expires_in)
        db.session.add(self)
        return self.token

    def revoke_token(self):
        """Method to revoke API token"""
        self.token_expiration = datetime.utcnow() - timedelta(seconds=1)

    @staticmethod
    def check_token(token):
        """Static method for token search and verification

        Args:
            token (str): Token to check

        Reurns:
            User : User to whom supplied token belongs to"""
        user = User.query.filter_by(token=token).first()
        if user is None or user.token_expiration < datetime.utcnow():
            return None
        return user
