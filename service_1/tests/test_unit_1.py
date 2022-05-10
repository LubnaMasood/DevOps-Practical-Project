from flask_testing import TestCase
from flask import url_for
import requests_mock 
from unittest.mock import patch

from application import app 


class TestBase(TestCase):
    def create_app(self):
        return app

class TestResponse(TestBase):
    def test_prizegenerator(self):
        with requests_mock.Mocker() as m:
            m.get('http://service_2:5000/randomnumber', text='2')
            m.get('http://service_3:5000/randomword', text='swimming')
            m.post('http://service_4:5000/service_4', json={
                "randomnumber": "3",
                "randomword": "netball",
                "prizestring": "3000"
            })
            
            response = self.client.get(url_for('prizegenerator'))
            self.assertEqual(response.status_code, 200)
            self.assertIn('netball', response.data.decode())
