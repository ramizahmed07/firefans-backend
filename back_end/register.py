from mysql.connector import MySQLConnection, Error, errors
from python_mysql_dbconfig import read_db_config
import collections
import json
import send_mail as mailer
import random
from media_handling import generate_check




def register_user(msg_received):
    fullName=msg_received["fullName"]
    userName=msg_received["userName"]
    email=msg_received["email"]
    phoneNo=msg_received["phoneNo"]
    password = msg_received["password"]
    random_number=random.randint(10000,99999)
    unique=str(generate_check.generate())

    dbconfig = read_db_config()
    conn = MySQLConnection(**dbconfig)
    cursor = conn.cursor()

    try:

        cursor.execute("INSERT INTO `user` (`user_id`, `fullName`, `userName`, `email`, `password`, `phoneNo`, `location`, `addition_date`) VALUES  (NULL, '"+fullName+"', '"+userName+"', '"+email+"', '"+password+"', '"+phoneNo+"', '', CURDATE())")
        conn.commit()
        cursor.execute("SELECT * FROM `user` WHERE `userName`='"+userName+"';")
        row = cursor.fetchall()
        for record in row:
          #print(str(record[0]))
          userID= str(record[0])

          cursor.execute("INSERT INTO `verification` (`verification_id`, `user_id`, `verification_code`,`created_at`,`verified`) VALUES  (NULL, '" + str(record[0]) + "','"+str(random_number)+"', NULL,'0');")
          conn.commit()
          mailer.sendVerification(email,userName,random_number)
          cursor.execute("INSERT INTO `subscription_price` (`subscription_id`, `user_id`, `subscription_price`,`currency`) VALUES  (NULL, '" + str(record[0]) + "','0','KES');")
          conn.commit()
          cursor.execute("INSERT INTO `profile_photo` (`pic_id`, `user_id`, `profile_pic`,`uniqueID` ) VALUES  (NULL, '" + str(record[0]) + "', 'null','"+unique+"');")
          conn.commit()
          cursor.execute("INSERT INTO `cover_photo` (`pic_id`, `user_id`, `cover_pic`,`uniqueID`) VALUES  (NULL, '" + str(record[0]) + "', 'null','"+unique+"');")
          conn.commit()
          cursor.execute("INSERT INTO `user_data` (`user_id`, `website`, `bio`,`tag_1`,`tag_2`,`tag_3`,`tag_4`,`tag_5`,`facebook`,`twitter`,`instagram`,`youtube`,`snapchat`,`tiktok`) VALUES  ('" + userID + "','','', '','','','','','www.facebook.com','www.twitter.com','www.instagram.com','www.youtube.com','www.snapchat.com','www.tiktok.com');")
          conn.commit()



        conn.close()
        cursor.close()
        return json.dumps({'notification':'success','verification':'sent'})

    except TypeError:
        conn.close()
        cursor.close()

        return json.dumps({"TypeError":"account not created"})

