from mysql.connector import MySQLConnection, Error
from python_mysql_dbconfig import read_db_config
import collections
import json
import tokens


def update_password(msg_received,header):
    password = msg_received["password"]
    user_id = tokens.getID(header)

    dbconfig = read_db_config()
    conn = MySQLConnection(**dbconfig)
    cursor = conn.cursor()

    if user_id == "Error expired token" or user_id == "Error invalid token":
        return json.dumps({'Error': 'login in again'})

    else:

        cursor.execute("SELECT * FROM `user` WHERE `password`='" + str(password) + "' AND `user_id`='"+str(user_id)+"';")
        row = cursor.fetchall()
        if len(row) == 1:

            conn.close()
            cursor.close()
            return json.dumps({'notification': 'password is correct'})

        else:
            conn.close()
            cursor.close()
            return json.dumps({'Error': 'password is not correct'})