"""error.py Error managment for API"""

# Flask modules(s)
from flask import jsonify
from werkzeug.http import HTTP_STATUS_CODES

from .app import app, db
from .utility import compile_response


def bad_request(text, status_code):
    """Response generator for bad request to API"""
    payload = {
        "error": HTTP_STATUS_CODES.get(status_code, "Unknown error"),
        "message": text,
    }
    response = jsonify(compile_response(description=payload))
    response.status_code = status_code
    return response


@app.errorhandler(404)
def not_found_error(error):
    """"""
    return bad_request("Not found", 404)


@app.errorhandler(500)
def internal_error(error):
    """"""
    db.session.rollback()
    return bad_request("Internal Server Error", 500)
