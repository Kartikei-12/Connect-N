from flask import jsonify
from werkzeug.http import HTTP_STATUS_CODES

from utility import compile_response


def bad_request(text, status_code):
    """"""
    payload = {
        "error": HTTP_STATUS_CODES.get(status_code, "Unknown error"),
        "message": text,
    }
    response = jsonify(compile_response(description=payload))
    response.status_code = status_code
    return response
