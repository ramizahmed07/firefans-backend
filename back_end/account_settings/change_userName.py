from mysql.connector import MySQLConnection, Error
from python_mysql_dbconfig import read_db_config
import collections
import json
import tokens

def update_userName(msg_received,header):
    userName = msg_received["userName"]
    user_id = tokens.getID(header)

    dbconfig = read_db_config()
    conn = MySQLConnection(**dbconfig)
    cursor = conn.cursor()

    if user_id == "Error expired token" or user_id == "Error invalid token":
        #print(header)
        conn.close()
        cursor.close()
        return json.dumps({'Error': 'login in again'})

    else:
        print(str(user_id))

        cursor.execute("SELECT * FROM `user` WHERE user_id='" + str(user_id) + "';")
        row = cursor.fetchall()
        if len(row) == 1:
            cursor.execute("UPDATE `user` SET `userName` = '" + str(userName) + "' WHERE user_id=" + str(user_id) + ";")
            conn.commit()
            conn.close()
            cursor.close()
            return json.dumps({'notification':'user name updated'})

        else:
            conn.close()
            cursor.close()
            return json.dumps({'Error':'user name not updated'})