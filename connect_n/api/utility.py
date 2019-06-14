"""Utility method(s) for Connect-N API"""

import json

from .env import RESPONSE_TEMPLATE


def compile_response(*args, **kwargs):
    """Function to compile response

    Returns:
        str : JSON response to API call"""
    response = RESPONSE_TEMPLATE.copy()
    for key, value in kwargs.items():
        response[str(key)] = value
    return json.dumps(response)
