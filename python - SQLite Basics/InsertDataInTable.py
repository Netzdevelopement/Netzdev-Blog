import sqlite3

connection = None
sqlSyntax = """ INSERT INTO user(name,username,email)
              VALUES(?,?,?) """
data = ["Philipp", "Philipp1297", "info@netzdev.de"]
try:
    connection = sqlite3.connect("testDatabase.db")
    curser = connection.cursor()
    curser.execute(sqlSyntax, data)
    connection.commit()

except:
    print("Error Connection to the Database")
finally:
    if connection:
        connection.close()