# install MySQL on my pc
# pip install mysql-connector
# pip install mysql-connector-python

import mysql.connector 

dataBase = mysql.connector.connect(
    host = 'localhost', 
    user = 'root', 
    password = 'password1234', 
)

# prepare a cursor object
cursorObject = dataBase.cursor()

# create a database
cursorObject.execute('CREATE DATABASE hava')

print('ALL Done!')