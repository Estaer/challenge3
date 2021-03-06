from api.database.db import Connection

import psycopg2
import datetime
from flask_jwt_extended import create_access_token
from flask_restful import request


class RideModel:
    """class that handles all major operations on rides"""

    def get_rides(self):
        """method to return all ride offers"""
        connection = Connection()
        cursor = connection.cursor
        cursor.execute("SELECT * from rides")
        rows = cursor.fetchall()
        ride_rows = []
        for row in rows:
            ride = {
                    "ride_id" : row[0],
                    "user_id" : row[1],
                    "meetingpoint": row[2].strip(),
                    "departure" : row[3].strftime("%Y-%m-%d %H:%M"),
                    "destination" : row[4].strip(),
                    "slots" : row[5]
            }
            ride_rows.append(ride)
        return ride_rows

    def get_my_rides(self, user_id):
        """method to return all ride offers specific to user"""
        connection = Connection()
        cursor = connection.cursor
        cursor.execute("SELECT * from rides where user_id = %s ",(user_id, ))
        rows = cursor.fetchall()
        ride_rows = []
        for row in rows:
            ride = {
                    "ride_id" : row[0],
                    "meetingpoint": row[2].strip(),
                    "departure" : row[3].strftime("%Y-%m-%d %H:%M"),
                    "destination" : row[4].strip(),
                    "slots" : row[5]
            }
            ride_rows.append(ride)
        return ride_rows
    
    def get_my_requests(self, user_id):
        """method to return all requests specific to user"""
        connection = Connection()
        cursor = connection.cursor
        cursor.execute("SELECT * from requests where user_id = %s ",(user_id, ))
        rows = cursor.fetchall()
        request_rows = []
        for row in rows:
            ride = {
                    "request_id" : row[0],
                    "ride_id": row[1],
                    "status" : row[3].strip()
                    
            }
            request_rows.append(ride)
        return request_rows


    def get_single_ride(self, ride_id):
        """ method to return a single ride offer """
        connection = Connection()
        cursor = connection.cursor
        cursor.execute("SELECT * FROM rides WHERE ride_id = %s",(ride_id, ))
        row = cursor.fetchone()
        if row:
            ride = {
                    "ride_id" : ride_id,
                    "user_id" : row[1],
                    "meetingpoint" : row[2].strip(),
                    "departure" : row[3].strftime("%Y-%m-%d %H:%M"),
                    "destination" : row[4].strip(),
                    "slots" : row[5]
                   }
            return ride
        else:
            return False

    def post_ride_offer(self, user_id):
        """ method to return a single ride offer """
        try:
            connection = Connection()
            cursor = connection.cursor
            data = request.get_json() 
            query = ("""INSERT into rides ( user_id, meetingpoint,
                            departure, destination, slots) 
                            VALUES(%s, %s, %s, %s, %s)""")
            cursor.execute(query, (user_id, 
                                    data["meetingpoint"], 
                                    data["departure"], 
                                    data["destination"],
                                    data["slots"]))
            return {"message":"Ride offer created"}

        except psycopg2.DataError as d:
             return {"message":"Invalid date format"}


    def check_existance(self, username):
        """method to check user existance prior to register"""
        connection = Connection()
        cursor = connection.cursor
        cursor.execute("SELECT * FROM users WHERE username = %s",(username, ))
        row = cursor.fetchone()
        if row:
            return True
        return False


    def register_user(self):
        """ method to register a user """
        connection = Connection()
        cursor = connection.cursor
        data = request.get_json()
        query = ("""INSERT into users ( firstname,
                        lastname, username, password)
                        VALUES(%s, %s, %s, %s)""")
        cursor.execute(query,(data["firstname"], data["lastname"], data["username"], data["password"]))
        sql = ("SELECT user_id from users where username = %s ")
        cursor.execute(sql, (data["username"], ))
        row = cursor.fetchone()
        if row:
            expire = datetime.timedelta(days=1)
            access_token = create_access_token(identity=row[0],expires_delta=expire)
            return access_token
        else:
            return False

    def login(self):
        """method to sign in a user"""
        connection = Connection()
        cursor = connection.cursor
        data = request.get_json()
        query = "SELECT * FROM users WHERE username = %s AND password = %s"
        cursor.execute(query,(data["username"], data["password"]))
        row = cursor.fetchone()
        if row:
            expire = datetime.timedelta(days=1)
            access_token = create_access_token(identity=row[0],expires_delta=expire)
            return access_token 
        else:
            return False

    def check_for_ride(self, ride_id):
        """method to check for a ride offer"""
        connection = Connection()
        cursor = connection.cursor
        query =  "SELECT * FROM rides WHERE ride_id = %s"
        cursor.execute(query, (ride_id, ))
        row = cursor.fetchone()
        if row:
            return True 
        else:
            return False

    def check_user_ride(self, ride_id, user_id):
        """method to check for a ride and corresponding user"""
        connection = Connection()
        cursor = connection.cursor
        query =  "SELECT * FROM rides WHERE ride_id = %s AND user_id = %s"
        cursor.execute(query, (ride_id,user_id))
        row = cursor.fetchall()
        if row:
            return True 
        else:
            return False


    def make_request(self, ride_id, user_id):
        """method to request for a ride offer"""
        connection = Connection()
        cursor = connection.cursor

        if (self.check_user_ride(ride_id,user_id)):
            return False
        else:
            query =  """INSERT into requests 
                        (ride_id, user_id, status) VALUES(%s, %s, %s)"""
            cursor.execute(query,(ride_id, user_id, "PENDING"))
            return True

    @staticmethod
    def check_username(ride_id):
        """method to map user id to a specific name"""
        connection = Connection()
        cursor = connection.cursor
        cursor.execute("SELECT username FROM users WHERE user_id = %s",(ride_id, ))
        row = cursor.fetchone()
        if row:
            return row[0]
        return ""

    def get_requests(self, ride_id):
        """method to return all requests for a given ride offer"""
        connection = Connection()
        cursor = connection.cursor
        cursor.execute("SELECT * from requests WHERE ride_id = %s",(ride_id, ))
        rows = cursor.fetchall()
        request_rows = []
        for row in rows:
            request = {
                    
                    "request_id" : row[0],
                    "ride_id": row[1],
                    "name" : RideModel.check_username(row[2]).strip(),
                    "status" : row[3].strip()
            }
            request_rows.append(request)
        return request_rows

    def check_for_request(self, ride_id, request_id):
        """method to check for a specific request """
        connection = Connection()
        cursor = connection.cursor
        data = request.get_json()
        query =  "SELECT * FROM requests WHERE ride_id=%s AND request_id=%s"
        cursor.execute(query, (ride_id, request_id))
        row = cursor.fetchone()
        if row:
            return True 
        else:
            return False

    def manage_request(self, ride_id, request_id):
        """ method to accept or reject a request """
        connection = Connection()
        cursor = connection.cursor
        data = request.get_json()
        query =  "UPDATE requests set status = %s WHERE ride_id=%s AND request_id=%s"
        cursor.execute(query,(data["status"], ride_id, request_id))
        return data["status"]
