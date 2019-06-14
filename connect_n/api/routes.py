"""API endpoints for Connect-N API"""

# Python module(s)
import json

# Flask module(s)
from flask import request, jsonify, g

# App module(s)
from .app import app, db
from .db_model import User
from .auth import token_auth
from .utility import compile_response
from .error import bad_request

# Project module(s)
from ..connect_n import ConnectNGame


@app.route("/", methods=["GET"])
@app.route("/test", methods=["GET"])
@app.route("/index", methods=["GET"])
def index():
    """API endpoint for index/homepage/testing"""
    return compile_response(description="Test Request")


@app.route("/new-user", methods=["POST"])
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


@app.route("/get-user/<int:id>", methods=["GET"])
@token_auth.login_required
def get_user(id):
    """API endpoint to retrive specefic user info from id"""
    u = User.query.get(id).to_dict() or {}
    response = jsonify(compile_response(user=u))
    response.status_code = 201
    return response


@app.route("/new-game", methods=["GET"])
@token_auth.login_required
def start_new_game():
    """"""
    user = User.query.get(g.current_user.id)
    if user.game != "Empty":
        return jsonify(
            compile_response(
                description="Previous game already in progress, try /delete to remove previous game"
            )
        )
    game = ConnectNGame()
    g.current_user.game = json.dumps(game.to_dict(), default=lambda x: x.__dict__)
    db.session.commit()
    response = jsonify(
        compile_response(description="New game created", game=g.current_user.game)
    )
    response.status_code = 201
    del game
    return response


@app.route("/get-game", methods=["GET"])
@token_auth.login_required
def get_game():
    """API endpoint to retrive current game"""
    user = User.query.get(g.current_user.id)
    game = user.game
    response = jsonify(compile_response(description="Game ended", game=game))
    response.status_code = 201
    return response


@app.route("/make-game/<int:move>", methods=["GET"])
@token_auth.login_required
def make_move(move):
    """API endpoit to make move in the game

    Args:
        move (int): Player move"""
    user = User.query.get(g.current_user.id)
    game_dict = json.loads(user.game)
    game = ConnectNGame()
    game.from_dict(game_dict)
    game.make_move(move, 2)
    user.game = json.dumps(game.to_dict())
    db.session.commit()
    response = jsonify(compile_response(description="Game ended", game=game.to_dict()))
    response.status_code = 201
    return response


@app.route("/end-game", methods=["GET"])
@token_auth.login_required
def end_game():
    """API endpoint to delete current game if any"""
    user = User.query.get(g.current_user.id)
    game = user.game
    user.game = "Empty"
    db.session.commit()
    response = jsonify(compile_response(description="Game ended", game=game))
    response.status_code = 201
    return response
