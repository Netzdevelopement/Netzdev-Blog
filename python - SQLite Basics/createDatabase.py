import sqlite3

connection = None
try:
    connection = sqlite3.connect("testDatabase.db")
except:
    print("Error Connection to the Database")
finally:
    if connection:
        connection.close()