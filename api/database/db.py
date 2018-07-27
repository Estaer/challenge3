import psycopg2
from flask import current_app


class Connection:
    def __init__(self,db=None):
        """ initialize the connection object """
        try:
            if db:
                self.my_connection = psycopg2.connect(database=db, user="postgres", password="postgres",
                                                      host="localhost", port="5432")
            else:
                if current_app.config["TESTING"]:
                    self.my_connection = psycopg2.connect(database="d4drt4pgjohc34", user="hbatljngbpftfl",
                                                          password="5b868ad02b6ac8634c3f947fc6e25a292d66055697d6d075874a71ee8e266f1a", host="ec2-54-243-59-122.compute-1.amazonaws.com", port="5432")
                else:
                    self.my_connection = psycopg2.connect(database="dfj524uvdi7ui7", user="xqjtwioxwfdfuo",
                                                          password="7398d44b7d43991c6f1256afbf56857c5e8e26d5e27a40264ec7d8ed297cb640", host="ec2-54-83-11-247.compute-1.amazonaws.com", port="5432")

            self.my_connection.autocommit = True
            self.cursor = self.my_connection.cursor()

            self.create_tables()
        except Exception as exp:
            print(exp)

    def query(self, query):
        """ method to execute an sql query """
        cursor = self.cursor
        cursor.execute(query)
        return cursor.fetchall()

    def close(self):
        """ method to close the database connection """
        self.my_connection.close()

    def drop_tables(self):
        self.cursor.execute("DROP TABLE if exists users cascade")
        self.cursor.execute("DROP TABLE if exists rides cascade")
        self.cursor.execute("DROP TABLE if exists requests cascade")

    def create_tables(self):
        self.cursor.execute("""CREATE TABLE IF NOT EXISTS rides
        (ride_id SERIAL PRIMARY KEY NOT NULL,
        user_id INT NOT NULL,
        meetingpoint CHAR(50) NOT NULL,
        departure TIMESTAMP NOT NULL,
        destination CHAR(50) NOT NULL,
        slots INT NOT NULL);""")

        self.cursor.execute("""CREATE TABLE IF NOT EXISTS requests
        (request_id SERIAL PRIMARY KEY NOT NULL,
        ride_id INT NOT NULL,
        user_id INT NOT NULL,
        status CHAR(50) NOT NULL
        );""")

        self.cursor.execute("""CREATE TABLE IF NOT EXISTS users
        (user_id SERIAL PRIMARY KEY NOT NULL,
        firstname CHAR(50) NOT NULL,
        lastname CHAR(50) NOT NULL,
        username CHAR(50) NOT NULL,
        password CHAR(50) NOT NULL
        );""")


if __name__ == "__main__":
    connect = Connection("dfj524uvdi7ui7")
    connect.create_tables()
