from unittest.mock import patch
from flask import url_for
from flask_testing import TestCase
import requests_mock
import jsonify

from application import app 

class TestBase(TestCase):
    def create_app(self):
        return app

class TestResponse(TestBase):
    def test_get_randomnumber(self):
        data = 



        {"letters" : 'ABCDE', "numbers" : '15'}