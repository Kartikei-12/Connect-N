"""API Utility Tests"""

# Python module(s)
import json
import unittest

# Project module(s)
from connect_n.api.utility import compile_response


class APIUtility(unittest.TestCase):
    """API utility method testing"""

    def test_compile_response(self):
        """Testing compile_response"""
        json_str = compile_response(test="test")
        json_dict = json.loads(json_str)
        self.assertEqual(json_dict["test"], "test")
        self.assertEqual(json_dict["description"], "")
