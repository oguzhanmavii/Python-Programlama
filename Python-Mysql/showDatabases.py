import mysql.connector

mydatabase=mysql.connector.connect(
    host='localhost',
    user='root',
    password='sifreni gir',
)

mycursor=mydatabase.cursor()
mycursor.execute('show databases')

for databases in mycursor:
    print(databases)
