"""auth.py file for Connect-N game API"""

# Flask module(s) and it's extentions
from flask import g
from flask_httpauth import HTTPBasicAuth, HTTPTokenAuth

# User module(s)
from .db_model import User
from .error import bad_request

token_auth = HTTPTokenAuth()
basic_auth = HTTPBasicAuth()


@basic_auth.verify_password
def verify_password(username, password):
    """API method used to verify password

    Args:
        username (str): Username
        password (str): Password for login

    Returns:
        bool : If valid password for supplied username"""
    user = User.query.filter_by(username=username).first()
    if user is None:
        return False
    g.current_user = user
    return user.check_password(password)


@basic_auth.error_handler
def basic_auth_error():
    """Error Handaler for Authorization Error"""
    return bad_request("Authorization Error", 401)


@token_auth.verify_token
def verify_token(token):
    """API token verification method"""
    g.current_user = User.check_token(token) if token else None
    return g.current_user is not None


@token_auth.error_handler
def token_auth_error():
    """Error Handaler for Authentication Error"""
    return bad_request("Authentication Error", 401)
