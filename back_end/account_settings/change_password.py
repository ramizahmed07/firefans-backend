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
        conn.close()
        cursor.close()
        return json.dumps({'Error': 'login in again'})

    else:

        cursor.execute("SELECT * FROM `user` WHERE user_id='" + str(user_id) + "';")
        row = cursor.fetchall()
        if len(row) == 1:
            cursor.execute("UPDATE `user` SET `password` = '" + str(password) + "' WHERE user_id=" + str(user_id) + ";")
            conn.commit()
            conn.close()
            cursor.close()
            return json.dumps({'notification': 'password updated'})

        else:
            conn.close()
            cursor.close()
            return json.dumps({'Error': 'password not updated'})