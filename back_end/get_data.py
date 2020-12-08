from mysql.connector import MySQLConnection, Error ,errors
from python_mysql_dbconfig import read_db_config
import collections
import json
import tokens

import io
from base64 import encodebytes
from PIL import Image

def getInfo(userID):
    details=[]
    tags=[]
    links={}
    #email = msg_received["email"]
    #phone_no = msg_received["email"]
    #pass_word = msg_received["password"]
    id_no=" "

    d = collections.OrderedDict()
    t = collections.OrderedDict()
    l=collections.OrderedDict()
    dbconfig = read_db_config()
    conn = MySQLConnection(**dbconfig)
    cursor = conn.cursor()
    try:

        cursor.execute("SELECT * FROM user where user_id='"+str(userID)+"';")
        row = cursor.fetchall()

        #while row is not None:
        if len(row) == 1:
            for record in row:
                #print(record)

              id_no=record[0]
              d['fullName'] = record[1]

              d['userName'] = record[2]

              d['location'] = record[6]

            cursor.execute("SELECT * FROM subscription_price where user_id = " + str(id_no))
            subscription = cursor.fetchall()
            if len(subscription) == 1:
                for record in subscription:
                    d['subscription_price'] = record[2]

            cursor.execute("SELECT * FROM profile_photo where user_id = " + str(id_no))
            profile_pic = cursor.fetchall()
            if len(profile_pic) == 1:
                for record in profile_pic:
                    d['profile_photo'] = record[2]

            cursor.execute("SELECT * FROM cover_photo where user_id = " + str(id_no))
            cover_pic = cursor.fetchall()
            if len(cover_pic) == 1:
                for record in cover_pic:
                    d['cover_photo'] = record[2]
                    d['uniqueID']= record[3]


            cursor.execute("SELECT * FROM user_data where user_id = '" + str(id_no) + "';")
            user_data = cursor.fetchall()
            if len(user_data) == 1:
                for info in user_data:
                    d['website'] = info[1]
                    d['bio'] = info[2]
                    tags = [info[3],info[4],info[5],info[6],info[7]]
                    links={'facebook':info[8],'twitter':info[9],'instagram':info[10],'youtube':info[11],'snapchat':info[12],'tiktok':info[13]}




            #print(json.dumps({'details': details}))
            conn.close()
            cursor.close()
            d['tags']=tags
            d['links']=links
            details.append(d)



            return json.dumps(details)

        else:
            conn.close()
            cursor.close()
            details_error= []
            #print("result set is empty")
            d = collections.OrderedDict()
            d['Error'] = "Record not fetched"
            details_error.append(d)
            return json.dumps(details_error)

    except (Error,UnboundLocalError,TypeError,errors) as e:
        print(e)
        conn.close()
        cursor.close()
        d[e]=e.args
        details.append(d)
        return json.dumps(details)

    finally:
        conn.close()
        cursor.close()






