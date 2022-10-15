import mysql.connector

# how to connect mysql database
mydatabase=mysql.connector.connect(
    host='localhost',
    user='root',
    password='sifreni gir',
    database='oguzhanmavi'
)
# how to create databases 
mycursor=mydatabase.cursor()


mycursor.execute('show tables')


for tables in mycursor:
    print(tables)