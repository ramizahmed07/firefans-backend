from mysql.connector import MySQLConnection, Error
from python_mysql_dbconfig import read_db_config
import collections
import json

def check_email(msg_received):
    email = msg_received["email"]

    dbconfig = read_db_config()
    conn = MySQLConnection(**dbconfig)
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM `user` WHERE `email`='" + email + "';")
    row = cursor.fetchall()

    if len(row) != 0:

        return json.dumps({'email':'1'})

    else:

        return json.dumps({'email':'0'})