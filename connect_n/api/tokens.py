"""API tokens handaling"""

from flask import jsonify, g

from .app import app, db
from .auth import basic_auth, token_auth
from .utility import compile_response


@app.route("/tokens", methods=["POST"])
@basic_auth.login_required
def get_token():
    """API endpoint to generate new token"""
    token = g.current_user.get_token()
    db.session.commit()
    return jsonify(compile_response(description={"token": token}))


@app.route("/tokens", methods=["DELETE"])
@token_auth.login_required
def revoke_token():
    """API endpoint to revoke user token"""
    g.current_user.revoke_token()
    db.session.commit()
    return "", 204
