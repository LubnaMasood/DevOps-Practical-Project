from unittest.mock import patch
from flask import url_for
from flask_testing import TestCase
import requests

from application import app, db
from application.models import Prize

class TestBase(TestCase):
    def create_app(self):
        app.config.update(SQLALCHEMY_DATABASE_URI = "sqlite:///")
        return app

    def setUp(self):
        db.create_all()
        db.session.add(Prize(diceroll="test", word="test", prizeamount="prizeamount"))
        db.session.commit()
    
    def tearDown(self):
        db.session.remove()
        db.drop_all()

class TestResponse(TestBase):
    def test_diceroll(self):
        with requests_mock.mock() as m:
            