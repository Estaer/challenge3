from db import Connection

connect = Connection()
cursor = connect.cursor

cursor.execute("""CREATE TABLE rides
        (ride_id SERIAL PRIMARY KEY NOT NULL,
        user_id INT NOT NULL,
        meetingpoint CHAR(50) NOT NULL,
        departure TIMESTAMP NOT NULL,
        destination CHAR(50) NOT NULL,
        slots INT NOT NULL);""")

cursor.execute("""CREATE TABLE requests
        (request_id SERIAL PRIMARY KEY NOT NULL,
        ride_id INT NOT NULL,
        user_id INT NOT NULL,
        status CHAR(50) NOT NULL
        );""")

print("Tables created successfully")
connect.my_connection.commit()
connect.my_connection.close()
