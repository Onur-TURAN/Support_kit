import mysql.connector

#hash tiplari md5 sha1 sha256 biri plmalı

mydb = mysql.connector.connect(
  host="localhost",
  user="yourusername",
  password="yourpassword",
    database="mydatabse"
)


def request(hash):
    mycursor=mydb.cursor()
    mycursor.execute("Select * From hashes")

    result=mycursor.fetchall()

    for x in result:
        print(x)