from db import Connection

connect = Connection()
cursor = connect.cursor

cursor.execute("DROP TABLE if exists rides")
cursor.execute("""CREATE TABLE rides
        (ride_id SERIAL PRIMARY KEY NOT NULL,
        user_id INT NOT NULL,
        meetingpoint CHAR(50) NOT NULL,
        departure TIMESTAMP NOT NULL,
        destination CHAR(50) NOT NULL,
        slots INT NOT NULL);""")
cursor.execute("DROP TABLE if exists requests")
cursor.execute("""CREATE TABLE requests
        (request_id SERIAL PRIMARY KEY NOT NULL,
        ride_id INT NOT NULL,
        user_id INT NOT NULL,
        status CHAR(50) NOT NULL
        );""")
cursor.execute("DROP TABLE if exists users")
cursor.execute("""CREATE TABLE users
        (user_id SERIAL PRIMARY KEY NOT NULL,
        firstname VARCHAR(50) NOT NULL,
        lastname VARCHAR(50) NOT NULL,
        username VARCHAR(50) NOT NULL,
        password VARCHAR(50) NOT NULL
        );""")

connect.my_connection.commit()
connect.my_connection.close()
print("Tables created successfully")