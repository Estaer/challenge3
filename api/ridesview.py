"""this contains methods for the api endpoints"""
from flask import jsonify
from flask_restful import Resource
from pprint import pprint
from .models.ride_details import All_Rides
from data.db import Connection

connection = Connection()
rides_object = All_Rides()
class Rides(Resource):
    """class for a Rides resource"""
    def get(self):
        """ method to fetch all ride offers """
        return jsonify({"result":rides_object.get_rides()})
        connection.close()

    def post(self):
        """ method to create ride offer """
        return jsonify({"result":rides_object.post_ride_offer()})
        connection.close()


class RideOffer(Resource):
     def get(self, ride_id):
        """returns a ride offer for a specific offer id"""
        return {"result":rides_object.get_single_ride(ride_id)}, 200
               
        