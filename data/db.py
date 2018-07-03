import psycopg2


class Connection:


    def __init__(self):
        """ initialize the connection object """
        self.my_connection = psycopg2.connect(
            database="testdb",
            user="postgres",
            password="postgres",
            host="127.0.0.1",
            port="5432")

        self.my_connection.autocommit = True
        self.cursor = self.my_connection.cursor()

    def query(self, query):
        """ method to execute an sql query """
        cursor = self.cursor
        cursor.execute(query)
        return cursor.fetchall()

    def close(self):
        """ method to close the database connection """
        self.my_connection.close()
