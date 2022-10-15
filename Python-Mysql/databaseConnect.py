import mysql.connector

# how to connect mysql database
mydatabase=mysql.connector.connect(
    host='localhost',
    user='root',
    password='rangers123',
    database='pythonExampledb'
)

