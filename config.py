import mysql.connector as sq# pip install mysql-connector-python

con=sq.connect(
    host="localhost",
    user="root",
    password="root",
    database="pydemo"
)
if con.is_connected():
    print("It is connected")
    print("details of con",type(con),"  ",con)
else:
    print("Not connected")
con.close()