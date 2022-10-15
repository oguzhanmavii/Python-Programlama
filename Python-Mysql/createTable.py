import mysql.connector

#establishing the connection
connections = mysql.connector.connect(
   user='root', password='sifreni gir',database='oguzhanmavi'
)

#Creating a cursor object using the cursor() method
mycursor = connections.cursor()

#Dropping EMPLOYEE table if already exists.
#mycursor.execute("DROP TABLE IF EXISTS EMPLOYEE")

#Creating table as per requirement
sql ='''CREATE TABLE EMPLOYEE(
   FIRST_NAME CHAR(20) NOT NULL,
   LAST_NAME CHAR(20),
   AGE INT,
   SEX CHAR(1),
   INCOME FLOAT
)'''
mycursor.execute(sql)

#Closing the connection
connections.close()