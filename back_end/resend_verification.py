import smtplib, ssl

from email.header import Header
from email.utils import formataddr
from email.mime.text import MIMEText
import email.utils
from email.utils import formatdate
import json
from mysql.connector import MySQLConnection, Error ,errors
from python_mysql_dbconfig import read_db_config
import random




def resendVerification(msg_received):

    recipient = msg_received["email"]
    random_number = random.randint(10000, 99999)
    userName=""
    user_id=""


    dbconfig = read_db_config()
    conn = MySQLConnection(**dbconfig)
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM user where email = '" + recipient+"';")

    row = cursor.fetchall()
    if len(row) == 1:
        for record in row:

            port = 465

            # Create a secure SSL context
            context = ssl.create_default_context()

            msg = MIMEText('THIS IS YOUR VERIFICATION CODE '+str(random_number)+'.')

            msg['To'] = email.utils.formataddr((str(record[2]),recipient))
            msg['From'] = email.utils.formataddr(('Firefans','noreply@firefans.co'))
            msg['Subject'] = "VERIFICATION CODE"
            msg["Date"] = formatdate(localtime=True)

            #mail_sender =formataddr((str(Header('Finance Manager', 'utf-8')),"noreply@firefans.co"))
            try:

                with smtplib.SMTP_SSL("smtp.hostinger.com", port,context=context) as server:

                    #server.set_debuglevel(True)
                    server.login("noreply@firefans.co", "Inferno@2020")
                    server.sendmail("noreply@firefans.co",[recipient], msg.as_string())
                    #print("email sent")
                    cursor.execute("UPDATE `verification` SET `verification_code` = '"+str(random_number)+"' WHERE `user_id` ="+str(record[0])+";")
                    conn.commit()
                    conn.close()
                    cursor.close()
                    return json.dumps({"notification":"code sent"})


            except TypeError as err:
                return json.dumps({err: err.args})
        conn.close()
        cursor.close()

    else:
        conn.close()
        cursor.close()
        return json.dumps({"Error":"Email not registered"})









