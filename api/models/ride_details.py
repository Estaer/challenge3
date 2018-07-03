from data.db import Connection
from flask_restful import request

connection = Connection()
class All_Rides:
    

    def get_rides(self):
        """method to return all ride offers"""
        cursor = connection.cursor
        cursor.execute("SELECT * from rides")
        rows = cursor.fetchall()
        return rows

    def get_single_ride(self, ride_id):
        """ method to return a single ride offer """
        cursor = connection.cursor
        cursor.execute("SELECT * FROM rides WHERE ride_id = %s",[ride_id])
        row = cursor.fetchone()
        if row:
            ride = {
                    "ride_id" : ride_id,
                    "user_id" : row[1],
                    "meetingpoint" : row[2],
                    "departure" : row[3].strftime("%Y-%m-%d %H:%M"),
                    "destination" : row[4],
                    "slot" : row[5]
            }
            return ride 
        else:
            return {"message" : "Ride offer doesnot exist"}
    
    def post_ride_offer(self):
        """ method to return a single ride offer """
        cursor = connection.cursor
        data = request.get_json() 
        query = ("""INSERT into rides ( user_id, meetingpoint,
                        departure, destination, slots) 
                        VALUES(%s, %s, %s, %s, %s)""")
        cursor.execute(query,(data["user_id"], data["meetingpoint"], data["departure"], data["destination"], data["slots"]))
        return {"message": "Ride Offer created"}

    def register_user(self):
        """ method to register a user """
        cursor = connection.cursor
        data = request.get_json() 
        query = ("""INSERT into users ( firstname,
                        lastname, username, password) 
                        VALUES(%s, %s, %s, %s)""")
        cursor.execute(query,(data["firstname"], data["lastname"], data["username"], data["password"]))
        return {"message": "User registered"}