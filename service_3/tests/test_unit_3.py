from flask_testing import TestCase
from flask import url_for, Response
from unittest.mock import patch

from application import app 

class TestBase(TestCase):
    def create_app(self):
        return app

class TestResponse(TestBase):
    def test_randomword(self):
        with patch("random.choice") as random:
            random.return_value = "running"
            response = self.client.get(url_for('randomword'))
            self.assertIn('running', response.data.decode())