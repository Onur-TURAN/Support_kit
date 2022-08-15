import mysql.connector
import hashlib

#hash tiplari md5 sha1 sha256 biri plmalı
'''
mydb = mysql.connector.connect(
  host="localhost",
  user="yourusername",
  password="yourpassword",
    database="mydatabse"
)


def SQL_request(hash):
    mycursor=mydb.cursor()
    mycursor.execute("Select * From hashes")

    result=mycursor.fetchall()

    for x in result:
        print(x)
'''

def hashing(file_name):
    hash_value=hashlib.md5(open(file_name,'rb').read()).hexdigest()
    print(hash_value)
    return hash_value

