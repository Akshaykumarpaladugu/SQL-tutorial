# importing required libraries
import mysql.connector


#trying to establish the connection between sever and python 
dataBase = mysql.connector.connect(
host ="localhost",
user ="root",
passwd ="",
)

# preparing a cursor object
cursorObject = dataBase.cursor()

# creating database
try:
    cursorObject.execute("CREATE DATABASE pythonc")
    print("done scuessfully",cursorObject)

except:
    print("cannot create database of :",cursorObject)


cursorObject.close()
