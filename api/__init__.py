from flask import Flask, request
from flask_restful import Resource, Api
from api.ridesview import Rides

app = Flask(__name__)
api = Api(app)

api.add_resource(Rides, '/api/v1/rides')
