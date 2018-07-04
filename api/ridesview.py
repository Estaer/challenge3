"""this contains methods for the api endpoints"""
from flask import jsonify
from flask_restful import Resource, request
from pprint import pprint
from .models.ride_details import All_Rides
from data.db import Connection

connection = Connection()
rides_object = All_Rides()
class Rides(Resource):
    """class for a Rides resource"""
    def get(self):
        """ method to fetch all ride offers """
        return {"result":rides_object.get_rides()}, 200
        connection.close()

    def post(self):
        """ method to create ride offer """
        return {"result":rides_object.post_ride_offer()}, 201
        connection.close()


class RideOffer(Resource):
    def get(self, ride_id):
        """returns a ride offer for a specific offer id"""
        return {"result":rides_object.get_single_ride(ride_id)}, 200
               
class Register(Resource):
    def post(self):
        """ method to register a user """
        return {"result":rides_object.register_user()}, 201
        connection.close()        

class Login(Resource):
    def post(self):
        """ method to sign in a user """
        if rides_object.login():
            return{"Message": "Success"}, 200
        else:
            return {"Message":"User does not exist"}, 404
        connection.close()

class MakeRequest(Resource):
    def post(self, ride_id):
        """ method to make a request for a ride """
        if rides_object.check_for_ride(ride_id):
            rides_object.make_request(ride_id)
            return {"Message":"Request successful"}
        else:
            return {"Message" : "Ride offer doesnot exist"}, 404
        connection.close()

    def get(self, ride_id):
        """ method to fetch all ride requests """
        return {"Available requests":rides_object.get_requests()}, 200
        connection.close()

    def put(self, ride_id, request_id):
        """ method to accept or reject a ride request """
        if rides_object.check_for_request(ride_id, request_id):
            status = rides_object.manage_request(ride_id, request_id)
            return {"Message":"Request {0}".format(status)}
        else:
            return {"Message" : "Ride request doesnot exist"}, 404
        connection.close()
        