from api import app
from api.database.db import Connection

import unittest
import json


class TestClass(unittest.TestCase):
    """ class containing methods to test the endpoints """
    def setUp(self):
        """ method to set up client """
        app.config["TESTING"] = True
        self.myapp = app.test_client()

        with app.app_context():
            connect = Connection()
            connect.drop_tables()
            connect.create_tables()
    
    # tests for valid urls
    
    def test_register_user(self):
        register_response = self.myapp.post("/auth/signup", data = json.dumps(dict(
                                                            firstname = "me",
                                                            lastname = "you",
                                                            username = "user6",
                                                            password = "hddhsd"
                                                            )),
                                                            content_type = 'application/json')
        self.assertEqual(register_response.status_code, 201)
        response_data = json.loads(register_response.data.decode())
        self.assertTrue(response_data["message"], "user registered")
        self.assertTrue(response_data["access_token"])
    
    def test_login(self):
        register_response = self.myapp.post("/auth/signup", data = json.dumps(dict(
                                                            firstname = "me",
                                                            lastname = "you",
                                                            username = "user2",
                                                            password = "hddhsd"
                                                            )),
                                                            content_type = 'application/json')

        login_response = self.myapp.post("/auth/login", data = json.dumps(dict(
                                                            username = "user2",
                                                            password = "hddhsd"
                                                            )),
                                                            content_type = 'application/json',
                                                            )
        response_data = json.loads(login_response.data.decode())
        self.assertTrue(response_data["message"], "Successfully logged in")
        self.assertTrue(response_data["access_token"])

    def test_get_all_rides(self):
        """method to test GET endpoints"""
        register_response = self.myapp.post("/auth/signup", data=json.dumps(dict(
            firstname="me",
            lastname="you",
            username="user3",
            password="hddhsd"
        )),
                                            content_type='application/json')
        register_data = json.loads(register_response.data.decode())
        access_token = register_data["access_token"]

        post_ride_response = self.myapp.post("/users/rides", headers=dict(Authorization="Bearer " + access_token),
                                             data=json.dumps(dict(
                                                 meetingpoint="buziga",
                                                 departure="2018-07-18 9:00",
                                                 destination="ggg",
                                                 slots=2)),
                                             content_type="application/json",
                                             )
        self.assertEqual(post_ride_response.status_code, 201)
        response_data = json.loads(post_ride_response.data.decode())
        self.assertTrue(response_data["message"], "Ride offer created")

        response = self.myapp.get("/rides")
        self.assertEqual(response.status_code, 200)

    def test_post_ride_offer(self):
        register_response = self.myapp.post("/auth/signup", data=json.dumps(dict(
            firstname="me",
            lastname="you",
            username="user3",
            password="hddhsd"
        )),
            content_type='application/json')
        register_data = json.loads(register_response.data.decode())
        access_token = register_data["access_token"]

        post_ride_response = self.myapp.post("/users/rides", headers=dict(Authorization="Bearer " + access_token),
                                             data=json.dumps(dict(
                                                 meetingpoint="buziga",
                                                 departure="2018-07-18 9:00",
                                                 destination="ggg",
                                                 slots=2)),
                                             content_type="application/json",
                                             )
        self.assertEqual(post_ride_response.status_code, 201)
        response_data = json.loads(post_ride_response.data.decode())
        self.assertTrue(response_data["message"], "Ride offer created")

    def test_get_single_ride(self):
        register_response = self.myapp.post("/auth/signup", data=json.dumps(dict(
            firstname="me",
            lastname="you",
            username="user3",
            password="hddhsd"
        )),
                                            content_type='application/json')
        register_data = json.loads(register_response.data.decode())
        access_token = register_data["access_token"]

        post_ride_response = self.myapp.post("/users/rides", headers=dict(Authorization="Bearer " + access_token),
                                             data=json.dumps(dict(
                                                 meetingpoint="buziga",
                                                 departure="2018-07-18 9:00",
                                                 destination="ggg",
                                                 slots=2)),
                                             content_type="application/json",
                                             )

        response = self.myapp.get("/rides/1", headers = dict(Authorization = "Bearer " + access_token))
        self.assertEqual(response.status_code, 200)

    def test_make_request(self):
        register_response = self.myapp.post("/auth/signup", data=json.dumps(dict(
            firstname="me",
            lastname="you",
            username="user4",
            password="hddhsd"
        )),
            content_type='application/json')
        register_data = json.loads(register_response.data.decode())
        access_token = register_data["access_token"]
        # 2nd user
        register_response2 = self.myapp.post("/auth/signup", data=json.dumps(dict(
            firstname="me",
            lastname="you",
            username="user5",
            password="hddhsd"
        )),
            content_type='application/json')
        register_data2 = json.loads(register_response2.data.decode())
        access_token2 = register_data2["access_token"]

        post_ride_response = self.myapp.post("/users/rides", headers=dict(Authorization="Bearer " + access_token),
                                             data=json.dumps(dict(
                                                 meetingpoint="buziga",
                                                 departure="2018-07-18 9:00",
                                                 destination="ggg",
                                                 slots=2)),
                                             content_type="application/json",
                                             )
        request_response = self.myapp.post("/rides/1/requests", headers=dict(Authorization="Bearer " + access_token2),

                                          content_type='application/json',
                                          )
        self.assertEqual(request_response.status_code, 201)
        response_data = json.loads(request_response.data.decode())
        self.assertTrue(response_data["message"], "Request successfully sent")

    def test_get_single_request(self):
        register_response = self.myapp.post("/auth/signup", data=json.dumps(dict(
            firstname="me",
            lastname="you",
            username="user4",
            password="hddhsd"
        )),
                                            content_type='application/json')
        register_data = json.loads(register_response.data.decode())
        access_token = register_data["access_token"]
        # 2nd user
        register_response2 = self.myapp.post("/auth/signup", data=json.dumps(dict(
            firstname="me",
            lastname="you",
            username="user5",
            password="hddhsd"
        )),
            content_type='application/json')
        register_data2 = json.loads(register_response2.data.decode())
        access_token2 = register_data2["access_token"]

        post_ride_response = self.myapp.post("/users/rides", headers=dict(Authorization="Bearer " + access_token),
                                             data=json.dumps(dict(
                                                 meetingpoint="buziga",
                                                 departure="2018-07-18 9:00",
                                                 destination="ggg",
                                                 slots=2)),
                                             content_type="application/json",
                                             )
        request_response = self.myapp.post("/rides/1/requests", headers=dict(Authorization="Bearer " + access_token2),

                                           content_type='application/json',
                                           )
        self.assertEqual(request_response.status_code, 201)
        response_data = json.loads(request_response.data.decode())
        self.assertTrue(response_data["message"], "Request successfully sent")

        response = self.myapp.get("/users/rides/1/requests")
        self.assertEqual(response.status_code, 200)

    def test_manage_request(self):
        register_response = self.myapp.post("/auth/signup", data=json.dumps(dict(
            firstname="me",
            lastname="you",
            username="user4",
            password="hddhsd"
        )),
                                            content_type='application/json')
        register_data = json.loads(register_response.data.decode())
        access_token = register_data["access_token"]
        # 2nd user
        register_response2 = self.myapp.post("/auth/signup", data=json.dumps(dict(
            firstname="me",
            lastname="you",
            username="user5",
            password="hddhsd"
        )),
            content_type='application/json')
        register_data2 = json.loads(register_response2.data.decode())
        access_token2 = register_data2["access_token"]

        post_ride_response = self.myapp.post("/users/rides", headers=dict(Authorization="Bearer " + access_token),
                                             data=json.dumps(dict(
                                                 meetingpoint="buziga",
                                                 departure="2018-07-18 9:00",
                                                 destination="ggg",
                                                 slots=2)),
                                             content_type="application/json",
                                             )
        request_response = self.myapp.post("/rides/1/requests", headers=dict(Authorization="Bearer " + access_token2),

                                           content_type='application/json',
                                           )
        self.assertEqual(request_response.status_code, 201)
        response_data = json.loads(request_response.data.decode())
        self.assertTrue(response_data["message"], "Request successfully sent")

        manage_request_response = self.myapp.put("/users/rides/1/requests/1", headers = dict(Authorization = "Bearer " + access_token),
                                                        data = json.dumps(dict(status = "Rejected")),
                                                            content_type = 'application/json')


        self.assertEqual(manage_request_response.status_code, 201)
        response_data = json.loads(manage_request_response.data.decode())
        self.assertTrue(response_data["status"], "Accepted")

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

    def tearDown(self):
        with app.app_context():
            connect = Connection()
            connect.drop_tables()
            connect.create_tables()


if __name__ == "__main__":
    unittest.main()
