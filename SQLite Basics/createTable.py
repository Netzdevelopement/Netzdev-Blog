import sqlite3

connection = None
sqlSyntax = """CREATE TABLE IF NOT EXISTS user (
        name text,
        username text,
        email text
        ); """
try:
    connection = sqlite3.connect("testDatabase.db")
    curser = connection.cursor()
    curser.execute(sqlSyntax)
except:
    print("Error Connection to the Database")
finally:
    if connection:
        connection.close()