from flask import Flask, request
from flask_restful import Resource, Api
from api.ridesview import Rides
from api.ridesview import RideOffer

app = Flask(__name__)
api = Api(app)

api.add_resource(Rides, '/api/v1/rides')
api.add_resource(RideOffer, '/api/v1/rides/<string:ride_id>')
