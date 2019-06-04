import json

from env import RESPONSE_TEMPLATE


def compile_response(*args, **kwargs):
    """"""
    response = RESPONSE_TEMPLATE.copy()
    for key, value in kwargs.items():
        response[key] = value
    return json.dumps(response)
