"""API endpoints for Connect-N API"""

from flask import request, jsonify

from app import app, db
from db_model import User

from utility import compile_response
from error import bad_request


@app.route("/", methods=["GET"])
@app.route("/test", methods=["GET"])
@app.route("/index", methods=["GET"])
def index():
    """API endpoint for index/homepage/testing"""
    return compile_response(description="Test Request")


@app.route("/users", methods=["POST"])
def create_user():
    """API endpoint to create new user"""
    data = request.get_json() or {}
    if "username" not in data or "email" not in data or "password" not in data:
        return bad_request("Must include username, email and password fields", 400)
    if User.query.filter_by(username=data["username"]).first():
        return bad_request("Please use a different username", 400)
    if User.query.filter_by(email=data["email"]).first():
        return bad_request("Please use a different email", 400)
    user = User()
    user.from_dict(data, new_user=True)
    db.session.add(user)
    db.session.commit()
    response = jsonify(compile_response(description=user.to_dict()))
    response.status_code = 201
    return response
