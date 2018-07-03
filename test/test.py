"""this contains test cases for the api endpoints"""
import unittest
import json
from run import app

class TestClass(unittest.TestCase):
    """ class containing methods to test the endpoints """
    def setUp(self):
        """ method to set up client """
        self.myapp = app.test_client()

    def test_get_endpoints(self):
        """method to test GET endpoints""" 
        response = self.myapp.get("/api/v1/rides")
        self.assertEqual(response.status_code, 200)

        response = self.myapp.get("/api/v1/rides/<string:ride_id>")
        self.assertEqual(response.status_code, 200)

if __name__ == "__main__":
    unittest.main()