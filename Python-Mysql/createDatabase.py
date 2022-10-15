import mysql.connector

# how to connect mysql database
mydatabase=mysql.connector.connect(
    host='localhost',
    user='root',
    password='sifreni gir',
)
# how to create databases 
mycursor=mydatabase.cursor()
mycursor.execute('create database newdatabase')
