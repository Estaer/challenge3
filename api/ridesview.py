"""this contains methods for the api endpoints"""
from flask import jsonify
from flask_restful import Resource
from data.db import Connection


class Rides(Resource):
    """class for a Rides resource"""
    def get(self):
        """method to return all ride offers"""
        connection = Connection()
        rides = connection.query("select * from rides"), 200
        connection.close()

        return jsonify({"result":rides})
