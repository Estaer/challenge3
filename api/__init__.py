"""This contains the libraries used and the endpoints"""
from flask import Flask, request
from flask_restful import Resource, Api
from flask_jwt_extended import (
    JWTManager, jwt_required, create_access_token,
    get_jwt_identity
)
from api.ridesview import Rides
from api.ridesview import RideOffer
from api.ridesview import Register
from api.ridesview import Login
from api.ridesview import MakeRequest

app = Flask(__name__)
app.config["JWT_SECRET_KEY"] = "GHFVJDFJKSNJKDVNKJSDNKVJJJNDJK"
jwt = JWTManager(app)
api = Api(app)

api.add_resource(Rides, "/rides", "/users/rides")
api.add_resource(RideOffer, "/rides/<int:ride_id>")
api.add_resource(Login, "/auth/login")
api.add_resource(Register, "/auth/signup")
api.add_resource(MakeRequest, "/users/rides/<int:ride_id>/requests",
                 "/rides/<int:ride_id>/requests",
                 "/users/rides/<int:ride_id>/requests/<int:request_id>")
