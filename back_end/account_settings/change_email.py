from mysql.connector import MySQLConnection, Error
from python_mysql_dbconfig import read_db_config
import collections
import json
import tokens
import send_mail
import random

def update_email(msg_received,header):
    email = msg_received["email"]
    user_id = tokens.getID(header)
    random_number = random.randint(10000, 99999)

    dbconfig = read_db_config()
    conn = MySQLConnection(**dbconfig)
    cursor = conn.cursor()

    if user_id == "Error expired token" or user_id == "Error invalid token":
        return json.dumps({'Error': 'login in again'})

    else:

        cursor.execute("SELECT * FROM `user` WHERE user_id='" + str(user_id) + "';")
        row = cursor.fetchall()
        if len(row) == 1:
            cursor.execute("UPDATE `user` SET `email` = '" + email + "' WHERE user_id=" + str(user_id) + ";")
            conn.commit()
            send_mail.sendVerification(email, row[2], random_number)
            cursor.execute("UPDATE `verification` SET ``verification_code`` = '"+random_number+"' WHERE user_id=" + str(user_id) + ";")
            conn.commit()
            cursor.execute("UPDATE `verification` SET `verified` = '0' WHERE user_id=" + str(user_id) + ";")
            conn.commit()
            conn.close()
            cursor.close()
            return json.dumps({'notification':'email updated'})

        else:
            conn.close()
            cursor.close()
            return json.dumps({'Error':'email not updated'})