import mysql.connector

dataBase = mysql.connector.connect(
    host = 'localhost',
    user = 'root',
    passwd = '1234'
)

# prepare a cursor object

cursorObject = dataBase.cursor()

cursorObject.execute("CREATE DATABASE nimplay2")

print("ALL DONE!")
