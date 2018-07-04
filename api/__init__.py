from flask import Flask, request
from flask_restful import Resource, Api
from api.ridesview import Rides
from api.ridesview import RideOffer
from api.ridesview import Register
from api.ridesview import Login
from api.ridesview import MakeRequest

app = Flask(__name__)
api = Api(app)

api.add_resource(Rides, "/rides", "/users/rides")
api.add_resource(RideOffer, "/rides/<string:ride_id>")
api.add_resource(Login, "/auth/login")
api.add_resource(Register, "/auth/signup")
api.add_resource(MakeRequest, "/users/rides/<string:ride_id>/requests", 
                                "/rides/<string:ride_id>/requests",
                                "/users/rides/<ride_id>/requests/<request_id>")
