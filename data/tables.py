from data.db import Connection

connect = Connection()
cursor = connect.cursor

cursor.execute("""CREATE TABLE RIDES
        (RIDEID INT PRIMARY KEY NOT NULL,
        USERID INT NOT NULL,
        MEETINGPOINT CHAR(50) NOT NULL,
        DEPARTURE TIMESTAMP NOT NULL,
        DESTINATION CHAR(50) NOT NULL,
        SLOTS INT NOT NULL);""")

cursor.execute("""CREATE TABLE REQUESTS
        (REQUESTID INT PRIMARY KEY NOT NULL,
        RIDEID INT NOT NULL,
        USERID INT NOT NULL,
        STATUS CHAR(50) NOT NULL
        );""")

print("Tables created successfully")
connect.my_connection.commit()
connect.my_connection.close()
