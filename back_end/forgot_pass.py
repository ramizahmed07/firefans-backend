from media_handling import picture_code
from mysql.connector import MySQLConnection, Error
from python_mysql_dbconfig import read_db_config
import json
import send_mail

def forgot_password(msg_received):

    email = msg_received["email"]
    code=picture_code.forgot_pass()

    dbconfig = read_db_config()
    conn = MySQLConnection(**dbconfig)
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM `user` WHERE email ='" + str(email) + "';")
    row = cursor.fetchall()

    if len(row)==1:
        for record in row:

            send_mail.sendVerification(email,record[2],code)
            cursor.execute("SELECT * FROM `reset` WHERE user_id ='" + str(record[0]) + "';")
            reset = cursor.fetchall()
            if len(reset)==0:
                cursor.execute("INSERT INTO `reset` (`id`, `user_id`, `reset`, `date`,`reset_value`) VALUES (NULL, '"+str(record[0])+"', '"+str(code)+"', CURRENT_TIMESTAMP,'0')")
                conn.commit()
                conn.close()
                cursor.close()
                return json.dumps({"success":"code sent"})

            else:
                cursor.execute("UPDATE `reset` SET `reset` = '" + str(code) + "' WHERE user_id=" + str(record[0]) + ";")
                conn.commit()
                conn.close()
                cursor.close()
                return json.dumps({"success": "code sent"})



    else:
        conn.close()
        cursor.close()
        return json.dumps({"Error": "please contact admin"})



def verify_pass_code(msg_received):
    code=msg_received["code"]
    email=msg_received["email"]

    dbconfig = read_db_config()
    conn = MySQLConnection(**dbconfig)
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM `user` WHERE email ='" + str(email) + "';")
    row = cursor.fetchall()

    if len(row) == 1:
        for record in row:

            cursor.execute("SELECT * FROM `reset` WHERE user_id ='" + str(record[0]) + "' AND reset='"+str(code)+"';")
            reset = cursor.fetchall()
            if len(reset) == 1:
                cursor.execute("UPDATE `reset` SET `reset_value` = '1' WHERE user_id='" + str(record[0])+"' AND reset='"+str(code)+"';")
                conn.commit()
                conn.close()
                cursor.close()
                return json.dumps({"success": "code accepted"})
            else:
                conn.close()
                cursor.close()
                return json.dumps({"Error": "contact admin"})
    else:
        conn.close()
        cursor.close()
        return json.dumps({"Error": "contact admin"})







