import random
from mysql.connector import MySQLConnection, Error
from python_mysql_dbconfig import read_db_config
import collections
import json
import tokens
import send_mail

def verify_email(msg_received,header):
    email = msg_received["email"]
    user_id = tokens.getID(header)
    random_number = random.randint(10000, 99999)

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
            for record in row:

                cursor.execute("SELECT * FROM `user` WHERE email='" + str(email) + "';")
                mails = cursor.fetchall()

                if len(mails) == 0:
                    send_mail.sendVerification(email, str(record[2]), random_number)
                    cursor.execute("UPDATE `verification` SET `verification_code` = '"+str(random_number)+"' WHERE user_id=" + str(user_id) + ";")
                    conn.commit()
                    cursor.execute("UPDATE `verification` SET `verified` = '2' WHERE user_id=" + str(user_id) + ";")
                    conn.commit()
                    conn.close()
                    cursor.close()
                    return json.dumps({'notification':'code sent'})
                else:
                    conn.close()
                    cursor.close()
                    return json.dumps({'Error': 'Email taken'})


        else:
            conn.close()
            cursor.close()
            return json.dumps({'Error':'code not sent'})