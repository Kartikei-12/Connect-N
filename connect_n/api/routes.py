from utility import compile_response

from api import app


@app.route("/", methods=["GET"])
@app.route("/test", methods=["GET"])
@app.route("/index", methods=["GET"])
def index():
    """View method for index/homepage"""
    return compile_response(description="Test Request")


def bad_request():
    """"""
    return compile_response(description="Bad Request")
