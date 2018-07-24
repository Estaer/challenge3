from api.views.ridesview import Ride
from api.views.ridesview import RideOffer
from api.views.ridesview import Register
from api.views.ridesview import Login
from api.views.ridesview import MakeRequest

from flask import Flask
from flask import jsonify
from flask_restful import Api
from flask_jwt_extended import JWTManager
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

app.config["JWT_SECRET_KEY"] = "GHFVJDFJKSNJKDVNKJSDNKVJJJNDJK"
jwt = JWTManager(app)
api = Api(app)

app.config["DEBUG"] = True
app.config["TESTING"] = False
app.config.from_object(__name__)


@app.errorhandler(404)
def not_found(error):
    return jsonify({"message": error.description}), 404


api.add_resource(Ride, "/rides", "/users/rides")
api.add_resource(RideOffer, "/rides/<int:ride_id>")
api.add_resource(Login, "/auth/login")
api.add_resource(Register, "/auth/signup")
api.add_resource(MakeRequest, "/users/rides/<int:ride_id>/requests",
                 "/rides/<int:ride_id>/requests",
                 "/users/rides/<int:ride_id>/requests/<int:request_id>")



