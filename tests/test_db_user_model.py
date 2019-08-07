"""API database user model Tests"""

# Python module(s)
import time
import unittest

# Project module(s)
from connect_n.api.app import create_app, app, db
from connect_n.api.db_model import User


class UserModelCase(unittest.TestCase):
    """API Database User Model testing"""

    def setUp(self):
        """Setup"""
        self.app = create_app("")
        self.app_context = self.app.app_context()
        self.app_context.push()
        db.create_all()

    def tearDown(self):
        """Tear Down"""
        db.session.remove()
        db.drop_all()
        self.app_context.pop()

    def test_password_hashing(self):
        """Testing Password hashing"""
        u = User(username="susan")
        u.set_password("cat")
        self.assertFalse(u.check_password("dog"))
        self.assertTrue(u.check_password("cat"))

    def test_check_token(self):
        """Tesing token verification"""
        u = User(username="susan")
        token = u.get_token()
        self.assertIsNotNone(User.check_token(token))
        u.revoke_token()

    def test_token_expiration(self):
        """Testing token expiration"""
        u = User(username="susan")
        token = u.get_token(expires_in=1)
        time.sleep(2)
        self.assertIsNone(User.check_token(token))

    def test_to_dict(self):
        """"""
        u = User(username="susan", email="susan@example.com")
        db.session.add(u)
        db.session.commit()
        u_dict = u.to_dict(include_email=True)
        self.assertEqual("susan@example.com", u_dict["email"])
        u_dict = u.to_dict(include_email=False)
        self.assertNotIn("email", u_dict)
