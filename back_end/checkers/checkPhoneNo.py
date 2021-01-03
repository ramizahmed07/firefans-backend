from mysql.connector import MySQLConnection, Error
from python_mysql_dbconfig import read_db_config
import collections
import json

def check_phoneNo(msg_received):
    phoneNo = msg_received["phoneNo"]

    dbconfig = read_db_config()
    conn = MySQLConnection(**dbconfig)
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM `user` WHERE `phoneNo`='" + phoneNo + "';")
    row = cursor.fetchall()

    if len(row) != 0:

        conn.close()
        cursor.close()
        return json.dumps({'phoneNo':'1'})

    else:
        conn.close()
        cursor.close()
        return json.dumps({'userName':'0'})