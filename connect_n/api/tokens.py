from flask import jsonify, g
from app import db

from app import app
from auth import basic_auth, token_auth
from utility import compile_response


@app.route("/tokens", methods=["POST"])
@basic_auth.login_required
def get_token():
    """"""
    token = g.current_user.get_token()
    db.session.commit()
    return jsonify(compile_response(description={"token": token}))


@app.route("/tokens", methods=["DELETE"])
@token_auth.login_required
def revoke_token():
    g.current_user.revoke_token()
    db.session.commit()
    return "", 204
