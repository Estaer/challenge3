"""this contains methods for the api endpoints"""
from flask_restful import Resource, request
from flask_jwt_extended import (jwt_required, get_jwt_identity)
from data.db import Connection
from .models.ride_details import All_Rides


CONNECTION = Connection()
rides_object = All_Rides()


class Rides(Resource):
    """class for a Rides resource"""


    def get(self):
        """ method to fetch all ride offers """
        return {"Available ride offers":rides_object.get_rides()}, 200
        CONNECTION.close()

    @jwt_required
    def post(self):
        """ method to create ride offer """
        my_ride = get_jwt_identity()
        data = request.get_json()
        for records in data.values():
            if str(records).strip() == "":
                return {"message": "Fill in the empty fields"}
        return rides_object.post_ride_offer(), 201
        CONNECTION.close()


class RideOffer(Resource):
    """class for a RideOffer resource"""


    def get(self, ride_id):
        """returns a ride offer for a specific offer id"""
        return {"Ride":rides_object.get_single_ride(ride_id)}, 200


class Register(Resource):
    """class for a Register resource"""


    def post(self):
        """ method to register a user """
        data = request.get_json()
        for records in data.values():
            if records.strip() == "":
                return {"message": "Fill in the empty fields"}

        if not rides_object.check_existance(data["username"]):
            access_token = rides_object.register_user()
            return {"message": "User registered",
                    "access_token":access_token
                   }, 201

        return {
            "message": "Username already exists."
        }
        CONNECTION.close()


class Login(Resource):
    """class for a Login resource"""


    def post(self):
        """ method to sign in a user """
        access_token = rides_object.login()
        if rides_object.login():
            return {"message":"Successfully logged in",
                    "access_token":access_token
            }, 200
        else:
            return {"message":"Wrong username or password"}, 404
        CONNECTION.close()

class MakeRequest(Resource):
    """class for a MakeRequest resource"""


    @jwt_required
    def post(self, ride_id):
        """ method to make a request for a ride """
        data = request.get_json()
        for records in data.values():
            if str(records).strip() == "":
                return {"message": "Fill in the empty fields"}

        if rides_object.check_for_ride(ride_id):
            rides_object.make_request(ride_id)
            my_request = get_jwt_identity()
            return rides_object.make_request(ride_id), 201
        else:
            return {"Message" : "Ride offer doesnot exist"}, 404
        CONNECTION.close()

    def get(self, ride_id):
        """ method to fetch requests to aspecific ride"""
        return {"Available requests":rides_object.get_requests()}, 200
        CONNECTION.close()

    @jwt_required
    def put(self, ride_id, request_id):
        """ method to accept or reject a ride request """
        manage = get_jwt_identity()
        data = request.get_json()
        for records in data.values():
            if str(records).strip() == "":
                return {"message": "Fill in the empty fields"}

        if rides_object.check_for_request(ride_id, request_id):
            status = rides_object.manage_request(ride_id, request_id)
            return rides_object.manage_request(ride_id, request_id)
        else:
            return {"Message" : "Ride request doesnot exist"}, 404
        CONNECTION.close()
