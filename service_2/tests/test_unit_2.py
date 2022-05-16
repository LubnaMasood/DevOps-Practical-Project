from flask_testing import TestCase
from flask import url_for, Response
from unittest.mock import patch

from application import app 

class TestBase(TestCase):
    def create_app(self):
        return app

class TestResponse(TestBase):
    def test_randomnumber(self):
        with patch("random.randint") as random:
            random.return_value = "11"
            response = self.client.get(url_for('randomnumber'))
            self.assertIn('11', response.data.decode())

            random.return_value = "7"
            response = self.client.get(url_for('randomnumber'))
            self.assertIn('7', response.data.decode())

            random.return_value = "1"
            response = self.client.get(url_for('randomnumber'))
            self.assertIn('1', response.data.decode())