from flask import url_for
from flask_testing import TestCase
from application import app
import json

class TestBase(TestCase):
    def create_app(self):
        return app

class TestViews(TestBase):
    def test_get_prizestring(self):
        response = self.client.post(url_for('service_4'), json={"randomnumber": "1", "randomword": "surfing"})
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'You Loose!', response.data)

    def test_get_prizestring_basketball(self):
        response = self.client.post(url_for('service_4'), json={"randomnumber": "9", "randomword": "basketball"})
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'4500', response.data)

    def test_get_prizestring_boxing(self):
        response = self.client.post(url_for('service_4'), json={"randomnumber": "10", "randomword": "boxing"})
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'5000', response.data)

    def test_get_prizestring_badminton(self):
        response = self.client.post(url_for('service_4'), json={"randomnumber": "2", "randomword": "badminton"})
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'1000', response.data)    
  
    