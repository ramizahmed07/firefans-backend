from mysql.connector import MySQLConnection, Error
from python_mysql_dbconfig import read_db_config
import tokens
import json
import collections
import get_data




def edit_profile(msg_received,header):

    msg = {
        "subject": "edit profile",
        "data": {
            "userName": "hassan",
            "fullName": "hassan athmani",
            "subscription_price": "100",
            "bio": "i love coding",
            "location": "Nairobi",
            "website":"www.me.com",
            "cover_photo":"www.com",
            "profile_photo":"www.com",
            "tags": ["Tag1", "Tag2"],
            "links": {
                "facebook": "www.facebook.com",
                "twitter": "www.twitter.com"
            }
        }
    }
    data=msg_received["data"]
    tags=data["tags"]
    links=data["links"]


    fullName=data["fullName"]
    userName=data["userName"]
    location=data["location"]
    website=data["website"]
    subscription_price = data["subscription_price"]
    bio= data["bio"]
    facebook=links["facebook"]
    twitter=links["twitter"]
    instagram=links["instagram"]
    youtube=links["youtube"]
    snapchat=links["snapchat"]
    tiktok=links["tiktok"]
    cover_photo=data["cover_photo"]
    profile_photo=data["profile_photo"]

    userID=tokens.getID(header)

    facebook_response="0"
    twitter_response="0"
    instagram_response="0"
    youtube_response="0"
    bio_response="0"
    subscription_price_response="0"
    website_response="0"
    location_response="0"
    userName_response="0"
    fullName_response="0"

    details=[]
    tagsA=[]
    d = collections.OrderedDict()
    t= collections.OrderedDict()



    dbconfig = read_db_config()
    conn = MySQLConnection(**dbconfig)
    cursor = conn.cursor()

    if userID == "Error expired token" or userID == "Error invalid token":
        return json.dumps({'Error': 'login in again'})

    else:

        cursor.execute("SELECT * FROM `user` WHERE user_id='"+str(userID)+"';")
        row=cursor.fetchall()
        if len(row)==1:
            j=1
            cursor.execute("UPDATE `user_data` SET `facebook` = '" + str(facebook) + "' WHERE user_id=" + str(userID) + ";")
            conn.commit()
            facebook_response =str(cursor.rowcount)

            cursor.execute("UPDATE `user_data` SET `twitter` = '" + str(twitter) + "' WHERE user_id=" + str(userID) + ";")
            conn.commit()
            twitter_response=str(cursor.rowcount)

            cursor.execute("UPDATE `user_data` SET `instagram` = '" + str(instagram) + "' WHERE user_id=" + str(userID) + ";")
            conn.commit()
            instagram_response=str(cursor.rowcount)

            cursor.execute("UPDATE `user_data` SET `youtube` = '" + str(youtube) + "' WHERE user_id=" + str(userID) + ";")
            conn.commit()

            cursor.execute("UPDATE `user_data` SET `snapchat` = '" + str(snapchat) + "' WHERE user_id=" + str(userID) + ";")
            conn.commit()

            cursor.execute("UPDATE `user_data` SET `tiktok` = '" + str(tiktok) + "' WHERE user_id=" + str(userID) + ";")
            conn.commit()



            for tag in tags:
                cursor.execute("UPDATE `user_data` SET `tag_"+str(j)+"` = '" + str(tag) + "' WHERE user_id=" + str(userID) + ";")
                conn.commit()
                t["tag_"+str(j)] = str(cursor.rowcount)
                j+=1

            if not fullName.isspace():
                if fullName:
                    cursor.execute("UPDATE `user` SET `fullName` = '"+fullName+"' WHERE user_id="+str(userID)+";")
                    conn.commit()
                    fullName_response=str(cursor.rowcount)

                    #print("hello")
            if not userName.isspace():
                if userName:
                    cursor.execute("UPDATE `user` SET `userName` = '" + userName + "' WHERE user_id=" + str(userID) + ";")
                    conn.commit()
                    userName_response=str(cursor.rowcount)


            if not location.isspace():
                if location:
                    cursor.execute("UPDATE `user` SET `location` = '" + location + "' WHERE user_id=" + str(userID) + ";")
                    conn.commit()
                    location_response=str(cursor.rowcount)

            if not website.isspace():
                if website:
                    cursor.execute("UPDATE `user_data` SET `website` = '" + website + "' WHERE user_id=" + str(userID) + ";")
                    conn.commit()
                    website_response=str(cursor.rowcount)

            if not cover_photo.isspace():
                if cover_photo:
                    cursor.execute("UPDATE `cover_photo` SET `cover_pic` = '" + str(cover_photo) + "' WHERE user_id=" + str(userID) + ";")
                    conn.commit()

            if not profile_photo.isspace():
                if profile_photo:
                    cursor.execute("UPDATE `profile_photo` SET `profile_pic` = '" + str(profile_photo) + "' WHERE user_id=" + str(userID) + ";")
                    conn.commit()

            if subscription_price>0:
               cursor.execute("UPDATE `subscription_price` SET `subscription_price` = '" + str(subscription_price) + "' WHERE user_id=" + str(userID) + ";")
               conn.commit()
               subscription_price_response=str(cursor.rowcount)


            if not bio.isspace():
                if bio:
                    cursor.execute("UPDATE `user_data` SET `bio` = '" + bio + "' WHERE user_id=" + str(userID) + ";")
                    conn.commit()
                    bio_response=str(cursor.rowcount)

            #d["fullName"] = fullName_response
            #d["userName"] = userName_response
            #d["location"] = location_response
            #d["website"] = website_response
            #d["subscription_price"] = subscription_price_response
            #d["facebook"] = facebook_response
            #d["twitter"] = twitter_response
            #d["instagram"] = instagram_response
            #d["youtube"] = youtube_response
            #tagsA.append(t)
            #details.append(d)


            conn.close()
            cursor.close()

            return get_data.getInfo(userID)

        else:
            conn.close()
            cursor.close()
            return json.dumps({'Error':"invalid token"})














