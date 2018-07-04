"""this contains test cases for the api endpoints"""
import unittest
import json
from api import app

class TestClass(unittest.TestCase):
    """ class containing methods to test the endpoints """
    def setUp(self):
        """ method to set up client """
        self.myapp = app.test_client()
    
    # tests for valid urls
    def test_get_all_rides(self):
        """method to test GET endpoints""" 
        response = self.myapp.get("/rides")
        self.assertEqual(response.status_code, 200)

    def test_get_single_ride(self):
        response = self.myapp.get("/rides/5")
        self.assertEqual(response.status_code, 200)
    
    def test_get_single_request(self):
        response = self.myapp.get("/users/rides/1/requests")
        self.assertEqual(response.status_code, 200)
    
    def test_post_ride_offer(self):
        response = self.myapp.post("/users/rides", data = json.dumps(dict(
                                                            user_id = 2, 
                                                            meetingpoint = "buziga",
                                                            departure = '2018-07-18 9:00',
                                                            destination = 'ggg',
                                                            slots = 2)),
                                                            content_type = 'application/json')
        self.assertEqual(response.status_code, 201)
    
    def test_make_request(self):
        response = self.myapp.post("/rides/1/requests", data = json.dumps(dict(
                                                            user_id = 2)),
                                                            content_type = 'application/json')
        self.assertEqual(response.status_code, 201)
    
    def test_register_user(self):
        response = self.myapp.post("/auth/signup", data = json.dumps(dict(
                                                            firstname = "me",
                                                            lastname = "you",
                                                            username = "me",
                                                            password = "hddhsd"
                                                            )),
                                                            content_type = 'application/json')
        self.assertEqual(response.status_code, 201)

    def test_login(self):
        response = self.myapp.post("/auth/login", data = json.dumps(dict(
                                                            username = "me",
                                                            password = "hddhsd"
                                                            )),
                                                            content_type = 'application/json')

    #tests for invalid urls
    def test_get_invalid_get_url(self):
        response = self.myapp.get("/rides/h")
        self.assertEqual(response.status_code, 404)
    
    def test_get_invalid_post_offer_url(self):
        response = self.myapp.post("/users/rides/h")
        self.assertEqual(response.status_code, 404)

    def test_get_invalid_post_request_url(self):
        response = self.myapp.post("/rides/5h/requests")
        self.assertEqual(response.status_code, 404)
    
    def test_get_invalid_put_url(self):
        response = self.myapp.put("/users/rides/5/requests/h")
        self.assertEqual(response.status_code, 404)

if __name__ == "__main__":
    unittest.main()
