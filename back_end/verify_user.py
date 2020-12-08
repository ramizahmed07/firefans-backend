from mysql.connector import MySQLConnection, Error ,errors
from python_mysql_dbconfig import read_db_config
import json


def verify_user(msg_received):
    vcode = msg_received["code"]
    email = msg_received["email"]

    dbconfig = read_db_config()
    conn = MySQLConnection(**dbconfig)
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM user where email = '" +email +"';")
    userId =cursor.fetchall()
    if len(userId) == 1:
        for record in userId:

            cursor.execute("SELECT * FROM `verification` where `user_id` = '" + str(record[0]) + "';")

            row = cursor.fetchall()
            if len(row) == 1:
                for ver in row:
                    if ver[4] == '1':
                        conn.close()
                        cursor.close()
                        return json.dumps({"Error": "account already verified"})


                    else:
                        cursor.execute("UPDATE `verification` SET `verified` = '1' WHERE (`verification_code` ='"+str(vcode)+"' and `user_id`='"+str(record[0])+"');")
                        conn.commit()
                        conn.close()
                        cursor.close()
                        return json.dumps({"Notification": "success"})


            else:

                conn.close()
                cursor.close()
                return json.dumps({"Error": "code not in db "})

    elif len(userId)>1:
        conn.close()
        cursor.close()
        return json.dumps({"Error": "More than one user has this email in db "})

    else:
        conn.close()
        cursor.close()
        return json.dumps({"Error": "email not registered "})



