"""this contains views for the api endpoints"""
from flask_restful import Resource, request, reqparse
from flask_jwt_extended import (jwt_required, get_jwt_identity)
from data.db import Connection
from .models.ride_details import RideModel


connection = Connection()
rides_object = RideModel()


class Ride(Resource):
    """class for a Ride resource"""


    def get(self):
        """ method to fetch all ride offers """
        return {"Available ride offers":rides_object.get_rides()}, 200
        connection.close()

    @jwt_required
    def post(self):
        """ method to create ride offer """
        args_parser = reqparse.RequestParser()
        args_parser.add_argument("meetingpoint", type=str, required=True)
        args_parser.add_argument("departure", type=str, required=True)
        args_parser.add_argument("destination", type=str, required=True)
        args_parser.add_argument("slots", type=str, required=True)
        args_parser.parse_args()

        data = request.get_json()
        user_id = get_jwt_identity()
        for records in data.values():
            if str(records).strip() == "":
                return {"message": "Fill in the empty fields"}, 400
        return rides_object.post_ride_offer(user_id), 201
        connection.close()


class RideOffer(Resource):
    """class for a RideOffer resource"""


    def get(self, ride_id):
        """returns a ride offer for a specific offer id"""
        if rides_object.get_single_ride(ride_id):
            return {"Ride":rides_object.get_single_ride(ride_id)}, 200
        else:
            return {"message" : "Ride offer doesnot exist"}, 404
        


class Register(Resource):
    """class for a Register resource"""


    def post(self):
        """ method to register a user """
        data = request.get_json()
        args_parser = reqparse.RequestParser()
        args_parser.add_argument("firstname", type=str, required=True)
        args_parser.add_argument("lastname", type=str, required=True)
        args_parser.add_argument("username", type=str, required=True)
        args_parser.add_argument("password", type=str, required=True)
        args_parser.parse_args()
        for records in data.values():
            if records.strip() == "":
                return {"message": "Fill in the missing fields"}, 400

        if not rides_object.check_existance(data["username"]):
            access_token = rides_object.register_user()
            return {"message": "User registered",
                    "access_token":access_token
                   }, 201

        return {"message": "Username already exists."}, 405
        connection.close()


class Login(Resource):
    """class for a Login resource"""


    def post(self):
        """ method to sign in a user """
        args_parser = reqparse.RequestParser()
        args_parser.add_argument("username", type=str, required=True)
        args_parser.add_argument("password", type=str, required=True)
        args_parser.parse_args()

        access_token = rides_object.login()
        if rides_object.login():
            return {"message":"Successfully logged in",
                    "access_token":access_token
                   }, 200
        else:
            return {"message":"Wrong username or password"}, 401
        connection.close()

class MakeRequest(Resource):
    """class for a MakeRequest resource"""


    @jwt_required
    def post(self, ride_id):
        """ method to make a request for a ride """
        user_id = get_jwt_identity()
        if rides_object.check_for_ride(ride_id):
            rides_object.make_request(ride_id, user_id)
            return rides_object.make_request(ride_id, user_id), 201
        else:
            return {"Message" : "Ride offer doesnot exist"}, 404
        connection.close()

    def get(self, ride_id):
        """ method to fetch requests to a specific ride"""
        if rides_object.get_requests(ride_id):
            requests = rides_object.get_requests(ride_id)
            return {"message":"Available requests",
                    "Requests": requests
                   }, 200
        else:
            return {"message":"No results found"}, 404
        connection.close()

    @jwt_required
    def put(self, ride_id, request_id):
        """ method to accept or reject a ride request """
        user_id = get_jwt_identity()
        data = request.get_json()
        for records in data.values():
            if str(records).strip() == "":
                return {"message": "Fill in the missing fields"}, 400

        if rides_object.check_for_request(ride_id, request_id):
            status = rides_object.manage_request(ride_id, request_id)
            return {"status": status,
                    "message":"Status updated successfully"}, 201
        else:
            return {"Message" : "Ride request doesnot exist"}, 404
        connection.close()
